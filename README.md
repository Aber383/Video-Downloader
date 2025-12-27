Video Downloader
A simple Python script to download YouTube videos in high quality using Python.

Features:
Downloads any YouTube video.
Shows the video title and view count before downloading.
Saves the video to a folder on your computer.

Requirements:
Python 3 installed (Windows, Mac, or Linux)
pytubefix package (a working version of Pytube)

Setup:
Download or clone this repository-
git clone https://github.com/Aber383/Video_Downloader.git
cd Video_Downloader

Install the required package:
py -m pip install pytubefix

How to Run:
Open a terminal in the project folder.
Run the script with a YouTube link as an argument-
py video.py "PASTE_YOUTUBE_LINK_HERE"


Example:
py video.py "https://youtu.be/vEQ8CXFWLZU"
The video will be saved in the folder specified in the script-
yd.download(r"C:\Users\ritap\OneDrive\Desktop\downloaded_videos")

Note: Make sure this folder exists before running the script.

Important Notes:
You must run it from the terminal — it won’t work with the Run button because it uses command-line arguments.
You don’t need to upload the downloaded videos folder to GitHub. The script saves files locally.

