#!/usr/local/bin/python
import bs4, requests
import sys
import pafy, vlc
from multiprocessing import Process

def ytsearch(args):    
    searchTerm= '+'.join(args)
    # print(searchTerm)
    text=requests.get('https://www.youtube.com/results?search_query='+searchTerm).text
    soup=bs4.BeautifulSoup(text,"lxml")

    div=[d for d in soup.find_all('div') if d.has_attr('class') and 'yt-lockup-dismissable' in d['class']]
    links=[]
    for d in div:
        img0=d.find_all('img')[0]
        a0=d.find_all('a')[0]
        links.append('http://www.youtube.com/'+a0['href'])
        imgL=img0['src'] if not img0.has_attr('data-thumb') else img0['data-thumb']
        a0=[ x for x in d.find_all('a') if x.has_attr('title')][0]
#        print((imgL, 'http://www.youtube.com/'+a0['href'],a0['title'])) 
        # print(links)
    return links[0]
#import subprocess
#def ytplay(link):
#    args=['google-chrome', str(link)]
#    p=subprocess.Popen(args)

class musicplay(Process):
    def __init__(self,link):
        Process.__init__(self)
        video=pafy.new(str(link))
        audio_url=video.getbestaudio().url
        self.p=vlc.MediaPlayer(audio_url)
    def run(self):
        self.p.play()
    def stop(self):
        self.p.stop()
        self.terminate()

class videoplay(Process):
    def __init__(self,link):
        Process.__init__(self)
        video=pafy.new(str(link))
        video_url=video.getbest().url
        self.p=vlc.MediaPlayer(video_url)
    def run(self):
        self.p.play()
    def stop(self):
        self.p.stop()
        self.terminate()
