import json
import os.path
import time

import requests
import re

totalPage = 13
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}
saveDir = 'I:/songs/'

# 获取周排行榜的歌曲
def getSongs():
    songs = {}
    pattern = r'<a\s+href="([^"]+)">\s*(.*?)\s*</a>'
    for i in range(totalPage):
        response = requests.get('https://www.gequbao.com/top/week-download', headers=headers, params={
            'page': f'{i}',
        })
        if response.status_code != 200:
            print(f'getSongs error: {response.text}')
            continue
        matches = re.findall(pattern, response.text)
        for match in matches:
            url, text = match
            if os.path.isfile(f'{saveDir}{text}.mp3'):
                continue
            print(f"URL: {url}")
            print(f"Text: {text}")
            songs[url] = text
        time.sleep(1.03)
    return songs

# 获取歌曲的播放url
def getSongsUrls(songs):
    songUrls = {}
    for key, value in songs.items():
        response = requests.get(f'https://www.gequbao.com{key}')
        pattern = r"window\.play_id\s*=\s*'([^']+)';"
        matches = re.search(pattern, response.text)
        response = requests.post('https://www.gequbao.com/api/play-url', data=json.dumps({'id': matches.group(1)}),
                                 headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            print(f'getSongsUrls error: {response.text}')
            continue
        try:
            jsonObj = response.json()
            print(f'song: {value} play_url: {jsonObj['data']['url']}')
            songUrls[jsonObj['data']['url']] = value
            time.sleep(1.03)
        except Exception as e:
            print(f'getSongsUrls error song : {value} key: key')
    return songUrls

# 下载歌曲
def downloadSongs(songs):
    for key, value in songs.items():
        with open(f'{saveDir}{value}.mp3', "wb") as file:
            response = requests.get(key)
            if response.status_code != 200:
                print(f'downloadSongs error: {response.text}')
                continue
            file.write(response.content)

downloadSongs(getSongsUrls(getSongs()))
# print(response.text)
