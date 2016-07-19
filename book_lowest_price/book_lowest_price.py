import requests
import webbrowser
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
	soup= BeautifulSoup(html, "lxml")
	ex= soup.find('div', attrs={'class' :"priceRow"})
	site_name= ex.find('div', attrs={'class' :"col-xs-4"})
	site_link = ex.find('a', attrs={'class': "btn btn-xs buyButton"})
	print ("Lowest Price Found ON : " + site_name.text)
	link_final = "https://www.vivilio.com" + site_link['href']
	print (link_final)
	webbrowser.open(link_final)

	#eex = ex.findAll('span', attrs={'class' :"titletext"})
	

def task_assign(url):
	html = get_requests(url)
	#print html
	parse_news(html)

def main():
	base_url= "https://www.vivilio.com/isbn/"
	isbn = int(input("Enter the isbn of the book you want to search: "))
	url = base_url + str(isbn)
	task_assign(url)


if __name__ == "__main__":
	main()
