from threading import Thread
import random 
import os,subprocess
import requests
import time
from bs4 import BeautifulSoup

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

def modify(name):
	words = name.split()
	ans = ""
	for word in words:
		ans = ans + word + "+"
	return ans

def get_imdb_rating(movie_name):
	try:
		headers={'User-Agent':"Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"}
		movie_name = modify(movie_name)
		url = "http://www.omdbapi.com/?t=" + movie_name + "&y=&plot=short&r=xml"
		r = requests.get(url, headers=headers)
		html = r.text.encode("utf8")
		soup = BeautifulSoup(html, "lxml")
		return soup.find('movie')['imdbrating']
	except:
		return "0"


def get_requests(url):
	file = open('thingy.txt', 'a')
	try:
		headers={'User-Agent':user_agents[random.randint(0,8)]}
		r = requests.get(url, headers=headers)
		html = r.text.encode("utf8")
		soup = BeautifulSoup(html, "lxml")
		ex = soup.findAll('table', attrs={'class': "wikitable"})
		try:
			xx=1
			for x in ex:
				movie_name = x.find('td').text
				rating = get_imdb_rating(movie_name)
				put = str(movie_name) + ";" + str(rating) + "\n"
				print (xx)
				xx+=1
				file.write(put)
		except:
			print ("Fuck the for loop")
	except :
		print ("Fuck the get_requests")
	file.close

def main():
  	url = "https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture"
  	final_list = get_requests(url)

if __name__ == '__main__':
	main()
