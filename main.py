import subprocess

image_file = 'your_image.jpg'  # your downloaded image filename here
stream_key = '0u91-thf0-2yca-3x17-3f39'

ffmpeg_command = [
    'ffmpeg',
    '-loop', '1',
    '-i', image_file,
    '-c:v', 'libx264',
    '-tune', 'stillimage',
    '-preset', 'veryfast',
    '-b:v', '2500k',
    '-maxrate', '2500k',
    '-bufsize', '5000k',
    '-pix_fmt', 'yuv420p',
    '-g', '50',
    '-c:a', 'aac',
    '-b:a', '128k',
    '-ar', '44100',
    '-f', 'flv',
    f'rtmp://a.rtmp.youtube.com/live2/{stream_key}'
]

subprocess.run(ffmpeg_command)
