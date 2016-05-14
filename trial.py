import requests
from bs4 import BeautifulSoup

def get_requests(url):
    print url
    r = requests.get(url)
    html = r.text.encode("utf8")
    soup = BeautifulSoup(html, "lxml").find('div',attrs={'id':"mw-content-text"})
    all_links = soup.findAll('a')
    final_links = []
    for link in all_links:
        try:
            if link['href'][0:5] == "/wiki":
               final_links.append(link)
        except:
            print "Sorry"
    return final_links[10:]

def check(links, target_url):
    for link in links: 
        if "https://en.wikipedia.org" + link['href'] == target_url:
            print "found"
            return True
    return False

width = 0

def get_width(start_url, target_url, flag, depth):
    global width
    if flag == True:
        print width
        return True
    if depth == 100:
        width=0
        return False
    links = get_requests(start_url)
    flag = check(links, target_url)
    if flag == False:
        width+=1
        for link in links:
            return get_width("https://en.wikipedia.org" + link['href'], target_url, flag, depth+1)
    else:
        print width
        return True
        

def main():
    start_url = "https://en.wikipedia.org/wiki/Presidential_system"
    target_url = "https://en.wikipedia.org/wiki/Delhi"    
    get_width(start_url, target_url, 0 , 0)
    

if __name__ == '__main__':
    main()