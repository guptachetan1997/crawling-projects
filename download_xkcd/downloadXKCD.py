import webbrowser
import os
import sys
import requests
from bs4 import BeautifulSoup
from threading import Thread


def get_requests(url):
	headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
	print (url)
	r = requests.get(url,headers = headers)
	r.raise_for_status()
	html = r.text.encode("utf8")
	soup = BeautifulSoup(html, "lxml")
	ex = soup.find('div',{'id':"comic"})
	eex = ex.find('img')
	if eex != None:
		comicURL = "http://www." + eex['src'][2:]
		res = requests.get(comicURL,headers=headers)
		imageFile = open(os.path.join('xkcd',os.path.basename(comicURL)),'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

threadlist = []

def main():
	base_url = "http://www.xkcd.com/"
	directory = "xkcd"
	if os.path.exists(directory) == False:
		os.makedirs('xkcd')
	ids = 1679
	j=1
	while ids>1600:
		j=0
		while j<= 6 and ids-j>5:
			url = base_url + str(ids)
			t = Thread(target=get_requests, args=(url,))
			t.start()
			threadlist.append(t)
			ids -=1
			j +=1
		for b in threadlist:
		 	b.join()



if __name__ == '__main__':
	main()

