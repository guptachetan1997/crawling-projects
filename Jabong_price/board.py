import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
import datetime
from bs4 import BeautifulSoup

#this could be a potentiol project for the summer to build a full grade price tracker
"""
	We can talk about the following things in the project:
		- Build the basic backend in Django/Python.
		- Use this script to get current prices
		- Learn about amazon products API and implement it to get a history of products
		- Learn about sending emails through python
		- Build a bare minimum frontend using html,css,js and jquery
		- Learn the basics of JS and JQuery.
"""

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
		file = open("curr.csv", 'a')
		timestamp = datetime.datetime.now()
		headers={'User-Agent':user_agents[random.randint(0,8)]}
		# headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
		r = requests.get(url,headers = headers)
		r.raise_for_status()  
		html = r.text.encode("utf8")  
		soup = BeautifulSoup(html, "lxml")
		ex = soup.find('span', attrs={'id':"priceblock_saleprice"})
		prices = (ex.text.split()[0]).split(',')
		total_price = ""
		for price in prices:
			total_price+=price
		file.write(str(timestamp) + ";" + total_price + "\n")
		file.close()
	except:
		print ("FUcked it")

def main():
	url = "http://www.amazon.in/WD-Passport-WDBGPU0010BBK-Portable-External/dp/B00Y0R9D6G?ie=UTF8"
	# url = "http://www.amazon.in/WD-Elements-Portable-External-Drive/dp/B008GS8LT0?ie=UTF8&qid=1460734887&ref_=sr_1_1&s=computers&sr=1-1"
	get_requests(url)

if __name__ == '__main__':
  main()

