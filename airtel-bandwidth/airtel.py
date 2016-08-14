import requests
from bs4 import BeautifulSoup

def get_ip_add(url):
	headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
	r = requests.get(url,headers = headers)
	r.raise_for_status()
	html = r.text.encode("utf8")
	soup = BeautifulSoup(html, "lxml")
	return str(soup.find('iframe')['src'])

def get_requests(url):
	headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
	r = requests.get(url,headers = headers)
	r.raise_for_status()
	html = r.text.encode("utf8")
	soup = BeautifulSoup(html, "lxml")
	ex =  soup.find('div', attrs={'class' : "box1"})
	eex = ex.find('ul')
	lis = eex.findAll('li')
	bandwidth_left = lis[1].find('div', attrs={'class':"description"}).find('span').text
	days_left = lis[2].find('div', attrs={'class':"description"}).find('span').text
	dsl = lis[3].find('div', attrs={'class':"description"}).find('span').text
	print ("Connection : " + dsl)
	print ("Bandwidth left : " + bandwidth_left)
	print ("Days Left : " + days_left)

def main():
	url = "http://www.airtel.in/smartbyte-s/page.html"
	fin_url = get_ip_add(url)
	get_requests(fin_url)

if __name__ == '__main__':
	main()

