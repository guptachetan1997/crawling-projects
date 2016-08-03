from selenium import webdriver
from selenium.webdriver.common.keys import Keys

contacts = []

driver = webdriver.Chrome()
driver.set_window_size(1120, 550)
driver.get("https://web.whatsapp.com/")

print('Enter batch name : ')
batch = input()

driver.find_element_by_xpath("//*[@id=\"side\"]/header/div[2]/div/span/div[2]/button").click()

driver.find_element_by_xpath("//*[@id=\"side\"]/header/div[2]/div/span/div[2]/span/div/ul/li[1]").click()

driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[1]/span[1]/span/div/div/div[2]/div/div[2]/div[1]/div").send_keys('2K16 ' + batch, Keys.RETURN)

for x in contacts:
	user_name = 'test' + str(x) + ' ' + batch
	driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[1]/span[1]/span/div/div/div[1]/div/div/input").send_keys(user_name, Keys.RETURN)

driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[1]/span[1]/span/div/div/span/button").click()

	
