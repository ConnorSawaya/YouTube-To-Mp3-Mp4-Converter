import os
import yt_dlp
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return "YouTube Downloader API is running! Use /download?url=YOUR_URL&ext=mp3"

@app.route('/download')
def download():
    url = request.args.get('url')
    ext = request.args.get('ext', 'mp3')

    if not url:
        return "Error: Missing URL parameter", 400

    # Output filename template
    out_template = 'downloaded_file.%(ext)s'
    
    ydl_opts = {
        'outtmpl': out_template,
        'noplaylist': True,
    }

    if ext == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts.update({'format': 'best[ext=mp4]'})

    try:
        # Clean up old files before downloading a new one
        if os.path.exists("downloaded_file.mp3"): os.remove("downloaded_file.mp3")
        if os.path.exists("downloaded_file.mp4"): os.remove("downloaded_file.mp4")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            # yt-dlp might change the extension during post-processing
            actual_filename = ydl.prepare_filename(info)
            if ext == 'mp3':
                actual_filename = actual_filename.rsplit('.', 1)[0] + '.mp3'
        
        return send_file(actual_filename, as_attachment=True)
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    # Get port from environment or default to 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
