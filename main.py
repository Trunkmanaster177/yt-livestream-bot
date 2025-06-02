import os

# Install gdown if not already installed
try:
    import gdown
except ImportError:
    os.system("pip install gdown")
    import gdown

# Google Drive file ID
file_id = "1PfbX9h03s-_PR9BjJZvC3wLmlfndv4yC"
video_file = "video.mp4"

# Download the video if not present
if not os.path.exists(video_file):
    print("Downloading video from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", video_file, quiet=False)
    print("Download complete.")

# YouTube stream key
stream_key = "a2wv-bcfa-167e-f4hr-eyx6"
rtmp_url = f"rtmp://a.rtmp.youtube.com/live2/{stream_key}"

# Start streaming using FFmpeg
print("Starting stream...")
os.system(
    f"ffmpeg -re -stream_loop -1 -i {video_file} "
    f"-c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k "
    f"-c:a aac -b:a 160k -ar 44100 -f flv {rtmp_url}"
)
