# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:22:06 2019

@author: Nayil
"""
from __future__ import unicode_literals
import urllib
import urllib.request
import json
import youtube_dl

# get_all_videos searches YouTube for all videos from my channel, parses the resulting JSON data,
#   and returns an array containing the video urls
# get_most_recent_video: None -> (listof String)
# side effects: variable mutation
def get_all_videos():
    
    api_key = 'AIzaSyCRYBoHC4L_CYeT9LaeG3hyIc1KQLD1owo'
    channel_id = 'UCsej4tgCoXDgVH3J7M3NMgw'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)
    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])
        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links

# download_all_videos downloads the MP3s for all YouTube vidoes from my channel.
# download_all_videos: (listof String) -> None
# side effects: downloads MP3s
def download_all_videos(links):
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for i in range(0, len(links)):
            ydl.download([links[i]])
    

def main():
    results = get_all_videos()
    download_all_videos(results)
        
if __name__ == "__main__":
    main()
        