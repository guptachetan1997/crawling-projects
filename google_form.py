from selenium import webdriver
from bs4 import BeautifulSoup
import time
from random import choice

driver = webdriver.Chrome() #getting to start the PhantomJS header webdriver using selenium
driver.set_window_size(1120, 550)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf46jnf6H3Yuv_-nbf9s3Cdyp7YPJGOuhFQkQkeN-sT-pERkg/viewform?c=0&w=1")

# Clicked the first Next Button
roll_no = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/input").send_keys("2K15/FU/999")
fn = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/input").send_keys("STOP")
ln = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/input").send_keys("STEALING")
gn = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[5]/div[2]/div/div[1]/div/div[1]/input").send_keys("DATA")
email = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[6]/div[2]/div/div[1]/div/div[1]/input").send_keys("FROM@US.COM")

driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[7]/div[2]/div[1]/div[1]/div[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[8]/div[2]/div[2]/div[3]/content").click()

driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[8]/div[2]/div/div[1]/div/div[1]/input").send_keys("9876543210")
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[9]/div[2]/div/div[1]/div/div[1]/input").send_keys("9876543210")

driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[10]/div[2]/div/div[1]/div/div[1]/input").send_keys("Kahin toh hoga")
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[11]/div[2]/div/div[1]/div/div[1]/input").send_keys("Kahin toh hoga")

driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[12]/div[2]/div[1]/div[1]/div[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[12]/div[2]/div[2]/div[3]/content").click()

driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[13]/div[2]/div/div[1]/div/div[1]/input").send_keys("100")
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[14]/div[2]/div/div[1]/div/div[1]/input").send_keys("100")

driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[15]/div[2]/div/div[1]/div/div[1]/input").send_keys("1/2/21")

driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[16]/div[2]/div/div[1]/div/div[1]/input").send_keys("Yahin hoon mai")


driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[17]/div[2]/div[1]/div[1]/div[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[19]/div[2]/div[2]/div[3]/content").click()

driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[20]/div[2]/div/div[1]/div/div[1]/input").send_keys("BHarat")
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[20]/div[2]/div/div[1]/div/div[1]/input").send_keys("Python")

driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[17]/div[2]/div[1]/div[1]/div[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div/div[2]/div[2]/div[19]/div[2]/div[2]/div[3]/content").click()



print("Clicked the first Next Button")

#driver.quit()
