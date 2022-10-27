#!/usr/bin/env python3
from time import time, mktime
from glob import glob
from datetime import datetime
import os
import feedparser
import yt_dlp

# Get the date when the script was last run
last_check = datetime.utcfromtimestamp(0)

if len(glob('downloads/last.txt')) != 0:
    with open('downloads/last.txt', 'r') as f:
        last_check = datetime.utcfromtimestamp(float(f.read()))

# Get all channels
channels = {}
with open('downloads/channels.txt') as f:
    for l in f.readlines():
        split = l.split(':')
        channels[split[0].strip()] = split[1].strip()

# Get all videos depending on the last time the script was run
videos = []
for key in channels:
    feed = feedparser.parse(
        'https://www.youtube.com/feeds/videos.xml?channel_id=' + channels[key]
    )
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

with open('downloads/last.txt', 'w') as f:
    f.write(str(time()))
