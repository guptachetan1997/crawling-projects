from threading import Thread
import time
import sys
import pyperclip
import requests
import webbrowser
import random
import os,subprocess
import sys
import pyperclip
import requests
from bs4 import BeautifulSoup
from time import gmtime, strftime

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

def get_requests(url,sym):
	name = sym + ".txt"
	files = open(name,"a")
	try:
		headers={'User-Agent':user_agents[random.randint(0,8)]}
		r = requests.get(url,headers = headers)
		r.raise_for_status()
		html = r.text.encode("utf8")
		soup = BeautifulSoup(html, "lxml")
		ex = soup.find('span',{'class':"time_rtq_ticker"})
		print (sym + " " + ex.text)
		time_stamp = strftime("%H:%M:%S", gmtime())
		files.write(str(str(time_stamp) + " " + ex.text + "\n"))
	except:
		get_requests(url,sym)
	files.close()

threadlist = []

def main():
	stock_symbol = open("stock_list.txt")
	symbol_list = stock_symbol.read()
	symbol_list = symbol_list.split()
	base_url = "http://finance.yahoo.com/q?s="
	while(1):
		try:
			for sym in symbol_list:
				url = base_url + sym
			 	t = Thread(target=get_requests, args=(url,sym))
			 	t.start()
			 	threadlist.append(t)
			for b in threadlist:
			 	b.join()
		except KeyboardInterrupt:
			pass
		print
		time.sleep(3)

if __name__ == '__main__':
	main()
