import requests
import random
from threading import Thread
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

def get_article(url,title,news):
	try:	
		headers={'User-Agent':user_agents[random.randint(0,8)]}
		r= requests.get(url, headers=headers)
		html= r.text.encode("utf8")
		soup = BeautifulSoup(html, "lxml")
		ex = soup.findAll('p')
		article = ""
		for x in ex:
			article += x.text
		news.append(dict(title=title, description=article))
	except:
		pass

threadlist = []

def get_requests(url):

	# headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
	try:
		news = []	
		headers={'User-Agent':user_agents[random.randint(0,8)]}
		r= requests.get(url, headers=headers)
		html= r.text.encode("utf8")
		soup = BeautifulSoup(html, "lxml")
		ex = soup.findAll('h2', attrs = {'class':"esc-lead-article-title"})
		i=0
		for x in ex:
			title = x.find('span').text
			news_artilce_url =  str(x.find('a')['href'])
			t = Thread(target=get_article, args=(news_artilce_url,title,news))
			t.start()
			threadlist.append(t)
		for b in threadlist:
			b.join()
		return news
	except:
		pass

def main():
	url= "https://news.google.co.in/"
	all_article_data = get_requests(url)
	for thing in all_article_data:
		print (thing['title'])


if __name__ == "__main__":
	main()
