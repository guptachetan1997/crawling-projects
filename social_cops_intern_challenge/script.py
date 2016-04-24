import requests
import pandas as pd
from bs4 import BeautifulSoup

def create_xml_from_api():
	filename = "trial"
	files = {'f': (filename+'.pdf', open(filename+'.pdf', 'rb'))}
	response = requests.post("https://pdftables.com/api?key=ebtz1w8lg4x1&format=xml", files=files)
	response.raise_for_status() # ensure we notice bad responses
	with open("example.xml", "wb") as f:
		f.write(response.content)

def send_soup():
	s = BeautifulSoup(open("/home/chetan/Desktop/example.xml"), "lxml").findAll('page')
	for page in s:
		parse_xml(page)


def parse_xml(soup):
	# r = requests.get("http://example.xml",)
	# xml = r.text.encode("utf8")
	# person = [][]
	person = [["" for x in range(7)] for x in range(30)]
	# soup = BeautifulSoup(open("/home/chetan/Desktop/example.xml"))
	ex = soup.findAll('tr')
	ex = ex[2:]
	length = len(ex)

	for j in range(0,10):
		for i in range(0,6):
			if i == 5:
				details = ex[i + j*6].findAll('td', attrs={'style':"text-align: right"})
				sex_detail = ex[i + j*6].findAll('td')
				idx = 0
				fuzzy_idx = 2
				for detail in details:
						try:
							person[idx + j*3][i] = detail.text.encode('utf-8')
							person[idx + j*3][i+1] = sex_detail[fuzzy_idx].text.encode('utf-8')
							if idx == 0:
								fuzzy_idx+=4
							else:
								fuzzy_idx+=3
						except IndexError:
							pass
						idx+=1
			else:
				details = ex[i + j*6].findAll('td')
				idx = 0
				for detail in details:
					if detail.text != "" and detail.text!="#":
						try:
							person[idx + j*3][i] = detail.text.encode('utf-8')
						except IndexError:
							pass
						idx+=1

	file  = open("thing.csv" ,"a")
	for ii in range(0,30):
		for jj in range(0,7):
			try:
				if jj>=2 and jj<=4 or jj == 6: 
					file.write(person[ii][jj].split(":")[1] + ";")
				else:
					file.write(person[ii][jj] + ";")
			except:
				print ii
				file.write(" " + ";")
		file.write("\n")
	file.close()

def main():
	file  = open("thing.csv" ,"a")
	file.write("id;serial;name;father/husband_name;house_no;age;sex\n")
	file.close()
	send_soup()

if __name__ == '__main__':
	main()
