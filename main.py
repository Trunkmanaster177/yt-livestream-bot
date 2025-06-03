import os
import time

while True:
    os.system("""
        ffmpeg -re -loop 1 -i your_image.png \
        -f lavfi -i anullsrc \
        -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k \
        -pix_fmt yuv420p -c:a aac -b:a 128k -g 50 \
        -shortest -f flv rtmp://a.rtmp.youtube.com/live2/0u91-thf0-2yca-3x17-3f39
    """)
    time.sleep(5)
