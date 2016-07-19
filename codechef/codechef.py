import requests
import subprocess
from bs4 import BeautifulSoup

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def get_requests(url):
	#headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
	r= requests.get(url) #headers=headers)
	html= r.text.encode("utf8")

	return html

def parse_news(html):
	print("The upcoming events on codechef are : ")
	print
	soup= BeautifulSoup(html,"lxml")
	ex= soup.find('div', attrs={'class' :"table-questions"})
	eex = ex.findAll('td')
	i=1
	stringer = ""
	for x in eex:
		#print x.text
		stringer = stringer + x.text + "\n"
		#stringer = stringer + "\n"
		if(i%4 == 0):
			#print stringer
			#stringer = ""
			stringer = stringer + "\n"
		i = i+1
	print (stringer)
	#sendmessage("upcoming codechef events ")

def task_assign(url):
	html = get_requests(url)
	#print html
	parse_news(html)

def main():
	url1= "https://www.codechef.com/contests"
	task_assign(url1)


if __name__ == "__main__":
	main()


