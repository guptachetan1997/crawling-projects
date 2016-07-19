import random 
import os,subprocess
import requests
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

def get_players_DOM(url):
	headers={'User-Agent':user_agents[random.randint(0,8)]}
	r = requests.get(url,headers = headers)
	r.raise_for_status()
	html = r.text.encode("utf8")
	soup = BeautifulSoup(html, "lxml")
	ex = soup.find('table', attrs={'class' : "engineTable"})
	players = ex.findAll('tr', attrs={'class':"data2"})
	return players

def check_DOM(dom_players, name):
	for player in dom_players:
		if player.find('td', attrs={'class':"left"}).text == name:
			return player
	return None

def get_players(url,url1):
	file = open("data-2013.csv","a")
	file.write("Name;Matches;Runs;Avg;SR\n")

	file1 = open("data-2013-DOM.csv","a")
	file1.write("Name;Matches;Runs;Avg;SR\n")

	headers={'User-Agent':user_agents[random.randint(0,8)]}
	r = requests.get(url,headers = headers)
	r.raise_for_status()
	html = r.text.encode("utf8")
	soup = BeautifulSoup(html, "lxml")
	ex = soup.find('table', attrs={'class' : "engineTable"})
	players = ex.findAll('tr', attrs={'class':"data2"})

	dom_players = get_players_DOM(url1)

	print (dom_players)
	for player in players:
		name =  player.find('td', attrs={'class':"left"}).text
		temp = player.findAll('td', attrs={'nowrap':"nowrap"})
		matches = player.find('td', attrs={'class':"padAst"}).text
		runs = temp[4].text
		avg = temp [6].text
		sr = temp[8].text
		dataline = name + ";" + matches + ";" + runs + ";" + avg + ";" + sr
		print (dataline)
		dataline += "\n"
		file.write(dataline)
		dom_player = check_DOM(dom_players, name)
		if dom_player is not None:
			name =  dom_player.find('td', attrs={'class':"left"}).text
			temp = dom_player.findAll('td', attrs={'nowrap':"nowrap"})
			runs = temp[4].text
			avg = temp [6].text
			sr = temp[8].text
			dataline = name + ";" + matches + ";" + runs + ";" + avg + ";" + sr
			dataline += "\n"
			file1.write(dataline)
	file.close()
	file1.close()

def main():
	url = "http://stats.espncricinfo.com/indian-premier-league-2013/engine/records/averages/batting.html?id=7720;type=tournament"
	url1 = "http://stats.espncricinfo.com/ci/engine/records/averages/batting.html?class=6;id=2013;type=year"
	get_players(url,url1)

if __name__ == '__main__':
	main()

