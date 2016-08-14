from selenium import webdriver
from selenium.webdriver.common.keys import Keys

contacts = [1,10,11,12,13,14,15,16,17,2,20,23,24,25,27,28,29,3,30,31,33,34,35,36,4,5,6,7,8,9]

driver = webdriver.Chrome()
driver.set_window_size(1120, 550)
driver.get("https://web.whatsapp.com/")

print('Enter batch name : ')
batch = input()

driver.find_element_by_xpath("//*[@id=\"side\"]/header/div[2]/div/span/div[2]/button").click()

driver.find_element_by_xpath("//*[@id=\"side\"]/header/div[2]/div/span/div[2]/span/div/ul/li[1]").click()

driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[1]/span[1]/span/div/div/div[2]/div/div[2]/div[1]/div").send_keys('2K16 ' + batch, Keys.RETURN)

for x in contacts:
	user_name = 'Target' + str(x) + ' ' + batch
	driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[1]/span[1]/span/div/div/div[1]/div/div/input").send_keys(user_name, Keys.RETURN)

driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[1]/span[1]/span/div/div/span/button").click()

	
