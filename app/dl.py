#!/usr/bin/env python3
from time import time, mktime
from glob import glob
from datetime import datetime
import os
import opml
import feedparser
import yt_dlp

# Create download folder if it doesn't exists
if not os.path.exists('downloads'):
    os.mkdir('downloads')

# Get the date when the script was last run
last_check = datetime.utcfromtimestamp(0)

if len(glob('last.txt')) != 0:
    f = open('last.txt', 'r')
    last_check = datetime.utcfromtimestamp(float(f.read()))
    f.close()

# Get all channels
urls = []
outline = opml.parse('downloads/subs.opml')
for o in outline[0]:
    urls.append(o.xmlUrl)

# Get all videos depending on the last time the script was run
videos = []
for url in urls:
    feed = feedparser.parse(url)
    for item in feed['items']:
        published = datetime.fromtimestamp(mktime(item['published_parsed']))
        if (published > last_check):
            videos.append(item['link'])

if len(videos) == 0:
    print('No new video found')
else:
    print(str(len(videos))+' new videos found')

    # Download the videos
    ydl_opts = {
        'ignoreerrors': True,
        'outtmpl': './downloads/%(uploader)s/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(videos)

f = open('last.txt', 'w')
f.write(str(time()))
f.close()
