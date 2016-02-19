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
import time
from bs4 import BeautifulSoup

score = "12"

user_agents = [  
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'
]

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def get_requests(url):
  try:
    headers={'User-Agent':user_agents[random.randint(0,8)]}
    # payload = {'username': 'admin', 'password' : 'admin'}
    # r = requests.post(url, data=payload)
    # print r.text
    r = requests.get(url,headers = headers)
    r.raise_for_status()  
    html = r.text.encode("utf8")  
    soup = BeautifulSoup(html)
    ex = soup.findAll('li',attrs = {'class':"regularitem"})
    for x in ex:
      print x
    # cur_score = str(ex[1].text)
    # print cur_score
    # global score
    # if(score != cur_score):
    #   score = cur_score
    #   sendmessage(score)
    # # for x in ex:
    # #   print x
  except:
    pass

threadlist = []

def main():
  url = "https://www.youtube.com/watch?v=tZRIDkpDKhg"
  get_requests(url)

if __name__ == '__main__':
  main()

