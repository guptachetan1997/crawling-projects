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

def parse_news(html):
	f = open("headline.txt","w")
	soup= BeautifulSoup(html, "lxml")
	ex= soup.find('div', attrs={'class' :"main-content-with-gutter-wrapper"})
	eex = ex.findAll('span', attrs={'class' :"titletext"})
	i=1
	j=1
	for x in eex:
		news_item = x.text
		if(j%2 != 0):
			f.write(str(i) + ". " + str(news_item) + "\n")
			i = i + 1
		j=j+1
	f.close()

def task_assign(url):
	html = get_requests(url)
	#print html
	parse_news(html)

def main():
	url1= "https://news.google.co.in/"
	task_assign(url1)


if __name__ == "__main__":
	main()
