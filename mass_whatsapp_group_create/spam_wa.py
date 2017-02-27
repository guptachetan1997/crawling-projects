from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options

#options = webdriver.ChromeOptions()
#options.add_argument("user-data-dir=/home/chetan/.config/google-chrome/Default") #Path to your chrome profile
#driver = webdriver.Chrome(executable_path="/opt/google/chrome/google-chrome",chrome_options=options)


driver = webdriver.Chrome()
driver.set_window_size(1120, 550)
driver.get("https://web.whatsapp.com/")

print('Enter target group name : ')
batch = input()
'''
driver.find_element_by_xpath("//*[@id=\"side\"]/header/div[2]/div/span/div[2]/button").click()

driver.find_element_by_xpath("//*[@id=\"side\"]/header/div[2]/div/span/div[2]/span/div/ul/li[1]").click()

driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[1]/span[1]/span/div/div/div[2]/div/div[2]/div[1]/div").send_keys(batch, Keys.RETURN)


for x in contacts:
	user_name = 'Target' + str(x) + ' ' + batch
	driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[1]/span[1]/span/div/div/div[1]/div/div/input").send_keys(user_name, Keys.RETURN)

driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[1]/span[1]/span/div/div/span/button").click()
'''
driver.find_element_by_xpath("//*[@id=\"side\"]/div[2]/div/label/input").send_keys('Didi', Keys.RETURN)

for x in range(10):
	driver.find_element_by_xpath("//*[@id=\"main\"]/footer/div[1]/div[1]/div/div[2]").send_keys('Unti')
	driver.find_element_by_xpath("//*[@id=\"main\"]/footer/div[1]/button[2]").click()
