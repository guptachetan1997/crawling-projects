import requests
import subprocess
from bs4 import BeautifulSoup

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def get_requests(url):
	headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
	r= requests.get(url, headers=headers)
	html= r.text.encode("utf8")

	return html

def parse_movie(html):
	soup= BeautifulSoup(html, "lxml")
	ex= soup.find('div', attrs={'id' :"pagecontent", 'class' :"pagecontent"})
	eex = ex.find('span', {'class' :"itemprop", 'itemprop' :"name"})
	eeex = ex.find('div', {'class' :"titlePageSprite star-box-giga-star"})
	print ("%s %s"%(eex.text,eeex.text))

def parse(html):
	soup= BeautifulSoup(html, "lxml")
	ex= soup.find('div', attrs={'class' :"lister"})
	eex = soup.findAll('td', attrs={'class' :"titleColumn"})
	for eeex in eex:
		temp = eeex.find('a')
		url =  "http://www.imdb.com" + temp['href']
		html = get_requests(url)
		parse_movie(html)

def task_assign(url):
	html = get_requests(url)
	#print html
	parse(html)

def main():
	url1= "http://www.imdb.com/chart/top?ref_=ft_250"
	task_assign(url1)


if __name__ == "__main__":
	main()
