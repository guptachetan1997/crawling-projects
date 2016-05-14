import requests
from bs4 import BeautifulSoup

main():
    r = requests.get("http://forum.ucweb.com/forum.php?mod=forumdisplay&fid=88&page=4")
    html = r.text.encode('utf8')
    print html
main
