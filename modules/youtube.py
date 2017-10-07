#!/usr/local/bin/python
import bs4, requests
import sys
def ytsearch(args):    
    searchTerm= '+'.join(args)
    text=requests.get('https://www.youtube.com/results?search_query='+searchTerm).text
    soup=bs4.BeautifulSoup(text)

    div=[d for d in soup.find_all('div') if d.has_attr('class') and 'yt-lockup-dismissable' in d['class']]
    links=[]
    for d in div:
        img0=d.find_all('img')[0]
        a0=d.find_all('a')[0]
        links.append('http://www.youtube.com/'+a0['href'])
        imgL=img0['src'] if not img0.has_attr('data-thumb') else img0['data-thumb']
        a0=[ x for x in d.find_all('a') if x.has_attr('title')][0]
#        print((imgL, 'http://www.youtube.com/'+a0['href'],a0['title'])) 
    return links[0]
import subprocess
def ytplay(link):
    args=['google-chrome', link]
    p=subprocess.Popen(args)
