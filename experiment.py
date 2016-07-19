import requests
from bs4 import BeautifulSoup

def get_requests(url):
    r = requests.get(url)
    r.raise_for_status()
    html = r.text.encode('utf8')
    soup = BeautifulSoup(html)
    print (soup)
    

main():
    r = requests.get("http://forum.ucweb.com/forum.php?mod=forumdisplay&fid=88&page=4")
    html = r.text.encode('utf8')
    print (html)
main
