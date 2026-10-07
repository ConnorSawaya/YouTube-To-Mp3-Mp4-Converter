# YouTube MP3 / MP4 Converter

A small Streamlit app for turning a YouTube link into a downloadable audio or video file.

Paste a YouTube URL, choose audio or video, let the app prepare the file, and download it directly from the Streamlit interface.

![Converter interface](https://github.com/user-attachments/assets/98f38114-ca6d-4640-95ac-9c5ad95c822c)

## Features

- Simple browser-based Streamlit interface.
- Audio-only and video download options.
- Shows the video's title and thumbnail before download.
- Uses `pytubefix` instead of requiring a YouTube API key.
- Removes the temporary server-side download after it is loaded for the user.

## Run locally

```bash
git clone https://github.com/ConnorSawaya/YouTube-To-Mp3-Mp4-Converter.git
cd YouTube-To-Mp3-Mp4-Converter
python -m pip install -r requirements.txt
streamlit run main.py
```

No API key is required.

## Project structure

```text
main.py            Streamlit application
requirements.txt   Python dependencies
Procfile           Railway start command
.env.example       Example environment file
```

## Deployment

The included `Procfile` is set up for a Streamlit deployment on Railway.

The app needs outbound internet access so `pytubefix` can retrieve the requested media.

## Notes

YouTube can change its delivery behavior over time, so downloader libraries may occasionally need to be updated. Only download media you are allowed to save and use.
