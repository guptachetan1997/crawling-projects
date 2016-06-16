from selenium import webdriver
from bs4 import BeautifulSoup
from django.template.defaultfilters import slugify
import time

driver = webdriver.PhantomJS()
time.sleep(4)
driver.set_window_size(1120, 550)
driver.get("http://www.hotstar.com/tv/shockers/9153/episodes/9038/9992")
html = driver.page_source
soup = BeautifulSoup(html.encode('utf8'), "lxml")
ex = soup.find_all('img', attrs={'ng-if':"record.urlPictures"})
for image in ex:
	print "http://www.hotstar.com/tv/shockers/9153/" + slugify(image['alt'][12:]) + "/" + image['src'][49:59]
driver.quit()
