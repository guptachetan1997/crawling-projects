import requests
import os, subprocess
import random
from bs4 import BeautifulSoup
from threading import Thread

ii=0
jj=0

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


def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return


def download_episode(episode_url):
    print (episode_url)
    os.system("wget -c \"" + episode_url + "\" >/dev/null 2>&1")


threadlist = []


def get_requests(url):
    base = "http://tv.dl-pars.in"
    try:
        headers = {'User-Agent': user_agents[random.randint(0, 8)]}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        html = r.text.encode("utf8")
        soup = BeautifulSoup(html, "lxml")
        ex = soup.findAll('a')
        i = 1
        for x in ex:
            if (x.text != "[To Parent Directory]"):
                season_url = base + x['href']
                print ("S0" + str(i))
                if i > 0:
                    res = requests.get(season_url, headers=headers)
                    htm = res.text.encode("utf8")
                    s = BeautifulSoup(htm, "lxml")
                    episode_list = s.find_all('a')
                    length = len(episode_list)
                    global ii
                    ii=1
                    while length > ii:
                        global jj
                        jj=0
                        while jj<4 and ii<length:
                            episode_url = base + episode_list[ii]['href']
                            t = Thread(target=download_episode, args=(episode_url,))
                            t.start()
                            threadlist.append(t)
                            jj+=1
                            ii+=1
                        for b in threadlist:
                            b.join()
                    print
                    print
                i+=1
    except:
        print ("hahahahhaha")


def main():
    #url = "http://dl2.filmha.org/Serial/Better%20Call%20Saul/"
    url = raw_input("Enter TV Series URL : ")
    get_requests(url)


if __name__ == '__main__':
    main()
