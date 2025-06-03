import os
import threading
from flask import Flask

# Install gdown if not already installed
try:
    import gdown
except ImportError:
    os.system("pip install gdown")
    import gdown

# Google Drive file ID
file_id = "1QLwRfy9p0kBWBWuWjjjZs79MdoRGEQiw"
video_file = "video.mp4"

# Download video if not already present
if not os.path.exists(video_file):
    print("Downloading video from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", video_file, quiet=False)
    print("Download complete.")

# YouTube stream key
stream_key = "krp8-ug6g-a8a0-9m5b-a9gd"
rtmp_url = f"rtmp://a.rtmp.youtube.com/live2/{stream_key}"

# FFmpeg livestream function
def start_stream():
    print("Starting stream...")
    os.system(
        f"ffmpeg -re -stream_loop -1 -i {video_file} "
        f"-vf scale=1280:720 -r 30 "
        f"-c:v libx264 -preset veryfast -b:v 2500k -maxrate 2500k -bufsize 5000k "
        f"-c:a aac -b:a 128k -ar 44100 "
        f"-f flv {rtmp_url}"
    )

# Flask app to keep service awake
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ YouTube livestream is running!"

# Run Flask server and FFmpeg in parallel
if __name__ == "__main__":
    threading.Thread(target=start_stream).start()
    app.run(host="0.0.0.0", port=10000)
