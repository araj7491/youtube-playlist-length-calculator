# YouTube Playlist Duration Calculator

A web application that calculates the total duration of all videos in a YouTube playlist using the YouTube Data API v3. Built with Flask and designed for easy deployment on Vercel.

## Features

• Calculate total duration of YouTube playlists  
• Display video count and formatted duration  
• Secure API key handling via environment variables  
• Ready for deployment on Vercel  
• Responsive web interface

## Demo

[Live Demo on Vercel](https://youtube-playlist-length-calculato-git-12965d-araj7491s-projects.vercel.app/)

## Local Development

### Prerequisites

- Python 3.7+
- YouTube Data API v3 key from [Google Cloud Console](https://console.cloud.google.com/)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/youtube-playlist-length-calculator.git
cd youtube-playlist-length-calculator
```

2. **Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your YouTube API key
```

5. **Run the application**
```bash
python app.py
```

6. **Open your browser and go to `http://localhost:5000`**

## Getting YouTube API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable YouTube Data API v3
4. Create credentials (API Key)
5. Restrict the key to YouTube Data API v3 for security

## Usage

1. Enter a YouTube playlist URL (e.g., `https://www.youtube.com/playlist?list=PLrAXtmRdnEQy-8qJCi4Fgz4c-3aTa4nfK`)
2. Click "Calculate Total Duration"
3. View the results showing total video count and duration

## Project Structure

```
youtube-playlist-length-calculator/
├── static/
│   └── style.css         # CSS styling
├── templates/
│   └── index.html        # HTML template
├── app.py                # Flask application
├── requirements.txt      # Python dependencies
├── vercel.json          # Deployment configuration
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## Technologies Used

• **Backend**: Python, Flask  
• **Frontend**: HTML5, CSS3, JavaScript  
• **API**: YouTube Data API v3  
• **Deployment**: Cloud Platform Ready  
• **Environment**: Virtual Environment (venv)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).