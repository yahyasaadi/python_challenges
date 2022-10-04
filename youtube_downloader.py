# pip install pytube
from pytube import YouTube

# provide the link of the video you want to download
yt = YouTube("https://www.youtube.com/watch?v=6Vaf3FD_PKQ")

# get the highest resolution possible
video = yt.streams.get_highest_resolution()

video.download('/home/yahya/Downloads/YouTube Videos')