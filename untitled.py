import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread
import sys
import pyperclip
import requests
import webbrowser
import random
import os,subprocess
import sys
import pyperclip
import requests
import datetime
from bs4 import BeautifulSoup

user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
  	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'
]

def modify_resolution(u):
    url = u
    url = url[:len(url)-13] + "_1920x1080.jpg"
    return url

def get_requests(url):
  try:
    headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
    r = requests.get(url,headers = headers)
    r.raise_for_status()
    html = r.text.encode("utf8")
    soup = BeautifulSoup(html)
    ex = soup.find('div',attrs={'id':"wallwindow"})
    eex = ex.find('img')
    source = eex.get('src')
    if source == "http://www.justinmaller.com/img/projects/wallpaper/":
        pass
    else:
        print source
        res = requests.get(source,headers = headers)
        imageFile = open(os.path.join('justinmaller',os.path.basename(source)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
  except:
    print "URL Invalid"

threadlist = []

def main():
  url = "http://justinmaller.com/wallpaper/"
  directory = "justinmaller"
  if os.path.exists(directory) == False:
      os.makedirs('justinmaller')
  for x in range(200,500):
    new_url = url + str(x) + "/"
    t = Thread(target=get_requests, args=(new_url, ))
    t.start()
    threadlist.append(t)
  for b in threadlist:
    b.join()

if __name__ == '__main__':
  main()
