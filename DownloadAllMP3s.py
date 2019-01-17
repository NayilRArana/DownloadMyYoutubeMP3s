# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:22:06 2019

@author: Nayil
"""

import urllib
import urllib.request
import json

# get_all_videos searches YouTube for all videos from my channel, parses the resulting JSON data,
#   and returns a tuple containing one array with the video urls and another with the video titles.
# get_most_recent_video: None -> tupleOf(listof String, listofString)
# side effects: variable mutation
def get_all_videos():
    
    api_key = 'AIzaSyCRYBoHC4L_CYeT9LaeG3hyIc1KQLD1owo'
    channel_id = 'UCsej4tgCoXDgVH3J7M3NMgw'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)
    video_links = []
    video_titles = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])
                video_titles.append(i["snippet"]["title"])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return (video_links, video_titles)

def main():
    results = get_all_videos()
    for i in range(len(results[0])):
        print(results[0][i])
        print(results[1][i])
        print("-------------------------")
        
if __name__ == "__main__":
    main()
        