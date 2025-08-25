from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import re
import requests
from datetime import timedelta
import isodate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

def extract_playlist_id(url):
    """Extract playlist ID from YouTube URL"""
    pattern = r'list=([a-zA-Z0-9_-]+)'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def parse_duration(duration):
    """Parse ISO 8601 duration format to seconds"""
    try:
        parsed = isodate.parse_duration(duration)
        return int(parsed.total_seconds())
    except:
        return 0

def format_duration(seconds):
    """Format seconds to human-readable duration"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"

def get_playlist_duration(playlist_id, api_key):
    """Calculate total duration of all videos in a playlist"""
    try:
        # First, get playlist details to fetch the playlist name
        playlist_details_url = f"https://www.googleapis.com/youtube/v3/playlists"
        playlist_details_params = {
            'part': 'snippet',
            'id': playlist_id,
            'key': api_key
        }
        
        response = requests.get(playlist_details_url, params=playlist_details_params)
        playlist_data = response.json()
        
        if 'error' in playlist_data:
            return None, f"API Error: {playlist_data['error']['message']}"
        
        if not playlist_data.get('items'):
            return None, "Playlist not found or is private"
        
        playlist_name = playlist_data['items'][0]['snippet']['title']
        
        # Get playlist items
        playlist_url = f"https://www.googleapis.com/youtube/v3/playlistItems"
        playlist_params = {
            'part': 'contentDetails',
            'playlistId': playlist_id,
            'maxResults': 50,
            'key': api_key
        }
        
        video_ids = []
        next_page_token = None
        
        # Get all video IDs from playlist (handle pagination)
        while True:
            if next_page_token:
                playlist_params['pageToken'] = next_page_token
                
            response = requests.get(playlist_url, params=playlist_params)
            data = response.json()
            
            if 'error' in data:
                return None, f"API Error: {data['error']['message']}"
            
            for item in data.get('items', []):
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)
            
            next_page_token = data.get('nextPageToken')
            if not next_page_token:
                break
        
        if not video_ids:
            return None, "No videos found in playlist"
        
        # Get video durations
        videos_url = f"https://www.googleapis.com/youtube/v3/videos"
        total_seconds = 0
        
        # Process videos in batches of 50
        for i in range(0, len(video_ids), 50):
            batch_ids = video_ids[i:i+50]
            video_params = {
                'part': 'contentDetails',
                'id': ','.join(batch_ids),
                'key': api_key
            }
            
            response = requests.get(videos_url, params=video_params)
            data = response.json()
            
            if 'error' in data:
                return None, f"API Error: {data['error']['message']}"
            
            for video in data.get('items', []):
                duration = video['contentDetails']['duration']
                total_seconds += parse_duration(duration)
        
        return {
            'playlist_name': playlist_name,
            'video_count': len(video_ids),
            'total_duration': format_duration(total_seconds),
            'total_seconds': total_seconds
        }, None
        
    except Exception as e:
        return None, f"Error: {str(e)}"

@app.route('/')
def index():
    result = session.pop('result', None)
    error = session.pop('error', None)
    return render_template('index.html', result=result, error=error)

@app.route('/calculate', methods=['GET'])
def calculate_get():
    return redirect('/')

@app.route('/calculate', methods=['POST'])
def calculate():
    playlist_url = request.form.get('playlist_url')
    
    if not playlist_url:
        session['error'] = "Please enter a playlist URL"
        return redirect('/')
    
    playlist_id = extract_playlist_id(playlist_url)
    if not playlist_id:
        session['error'] = "Invalid YouTube playlist URL"
        return redirect('/')
    
    # Get API key from environment variable for security
    api_key = os.environ.get('YOUTUBE_API_KEY')
    
    if not api_key:
        session['error'] = "YouTube API key not configured. Please set YOUTUBE_API_KEY environment variable."
        return redirect('/')
    
    result, error = get_playlist_duration(playlist_id, api_key)
    
    if error:
        session['error'] = error
        return redirect('/')
    
    session['result'] = result
    return redirect('/')

# This same file works for both local development and Vercel deployment

if __name__ == '__main__':
    app.run(debug=True)