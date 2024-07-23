import subprocess


def ffmpeg_mix():
    cmd = 'ffmpeg -y -i "audio.mp3"  -i "video.mp4" -filter:a aresample=async=1 -c:a flac -c:v copy output.mp4'
    subprocess.call(cmd, shell=True)
    print('Mixing Done')
