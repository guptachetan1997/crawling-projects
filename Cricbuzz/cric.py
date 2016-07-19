import requests
import random
import os,subprocess,time
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

def sendmessage(heading, message):
    os.system("notify-send \"" + heading + "\" \"" + message + "\" --urgency=critical")

def get_requested_id(url):
    try:
        headers={'User-Agent':user_agents[random.randint(0,8)]}
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        html = r.text.encode("utf8")
        soup = BeautifulSoup(html, "lxml")
        ex = soup.findAll('match')
        flag = 0
        for x in ex:
            if x.find('state')['mchstate'] == "inprogress":
                flag = 1
                print (x['mchdesc'] + " :id: " + x['id'])
        print
        if flag == 1:
            requested_id = input("Enter the id : ")
            return str(requested_id)
        else:
            return str("SORRY")
    except:
        pass

def get_requests(url, requested_id):
    try:
        headers={'User-Agent':user_agents[random.randint(0,8)]}
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        html = r.text.encode("utf8")
        soup = BeautifulSoup(html, "lxml")
        ex = soup.findAll('match')
        for x in ex:
            if x.find('state')['mchstate'] == "inprogress" and x['id'] == requested_id:
                print (x['mchdesc'])
                team = x.find("bttm")['sname']
                crr = ((x.find('mscr')).find('inngsdetail'))['crr']
                rrr = ((x.find('mscr')).find('inngsdetail'))['rrr']
                if rrr == "0":
                    score = str(team) + ": " + x.find('inngs')['r'] + "/" + x.find('inngs')['wkts'] + " OVRS: " + x.find('inngs')['ovrs'] + " Cur.RR: " + crr + "\n" + x.find('state')['status']
                else:
                    score = str(team) + ": " + x.find('inngs')['r'] + "/" + x.find('inngs')['wkts'] + " OVRS: " + x.find('inngs')['ovrs'] + " Req.RR: " + rrr + "\n" + x.find('state')['status']
                print (score)
                tagline  = x['mchdesc'] + "\n" + score
                sendmessage(x['mchdesc'], score)
    except:
        pass

def main():
    url = "http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
    requested_id = get_requested_id(url)
    if requested_id != "SORRY":
        while True:
            get_requests(url, requested_id)
            time.sleep(15)
    else:
        print ("No match is currently live.")

if __name__ == '__main__':
    main()

