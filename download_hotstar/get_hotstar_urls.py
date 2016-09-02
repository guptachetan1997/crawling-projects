from selenium import webdriver
from bs4 import BeautifulSoup
from django.template.defaultfilters import slugify
import time

driver = webdriver.PhantomJS() #getting to start the PhantomJS header webdriver using selenium
time.sleep(4)
print("driver set")
driver.set_window_size(1120, 550)
driver.get("http://www.hotstar.com/tv/the-numbers-game/6202/episodes/6119/9992")
print("driver get")
html = driver.page_source
soup = BeautifulSoup(html.encode('utf8'), "lxml")
ex = soup.find_all('img', attrs={'ng-if':"record.urlPictures"})
print("driver scraping content")
print(ex)
for image in ex:
	print ("http://www.hotstar.com/tv/the-numbers-game/6202/" + slugify(image['alt'][12:]) + "/" + image['src'][49:59])
driver.quit()
