# YouTube Playlist Duration Calculator

A simple web app to calculate the total duration of all videos in a YouTube playlist.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get a YouTube Data API key:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one
   - Enable YouTube Data API v3
   - Create credentials (API Key)
   - Replace `YOUR_YOUTUBE_API_KEY_HERE` in `app.py` with your actual API key

3. Run the application:
```bash
python app.py
```

4. Open your browser and go to `http://localhost:5000`

## Usage

1. Enter a YouTube playlist URL (e.g., `https://www.youtube.com/playlist?list=PLrAXtmRdnEQy-8qJCi4Fgz4c-3aTa4nfK`)
2. Click "Calculate Total Duration"
3. View the results showing total video count and duration

## Files

- `app.py` - Flask backend server
- `templates/index.html` - HTML frontend
- `static/style.css` - CSS styling
- `requirements.txt` - Python dependencies