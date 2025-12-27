from pytubefix import YouTube
from sys import argv
from urllib.parse import urlparse, parse_qs


link = argv[1]


parsed = urlparse(link)
video_id = parse_qs(parsed.query).get('v', [parsed.path.split('/')[-1]])[0]
clean_link = f"https://www.youtube.com/watch?v={video_id}"


yt = YouTube(clean_link)
print("Title:", yt.title)
print("Views:", yt.views)


yd = yt.streams.get_highest_resolution()
yd.download(r"C:\Users\ritap\OneDrive\Desktop\downloaded_videos")
