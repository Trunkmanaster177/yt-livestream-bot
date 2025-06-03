import os
import time

STREAM_KEY = os.getenv("0u91-thf0-2yca-3x17-3f39")  # use env var for security

while True:
    # FFmpeg command to loop an image forever
    os.system(f"""
        ffmpeg -re -loop 1 -i your_image.png \
        -f lavfi -i anullsrc \
        -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k \
        -pix_fmt yuv420p -c:a aac -b:a 128k -g 50 \
        -shortest -f flv rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}
    """)
    
    # Optional: wait before restarting if FFmpeg stops
    time.sleep(5)
