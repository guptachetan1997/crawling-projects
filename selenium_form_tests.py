from selenium import webdriver
from bs4 import BeautifulSoup
import time
from random import choice

driver = webdriver.Chrome() #getting to start the PhantomJS header webdriver using selenium
driver.set_window_size(1120, 550)
driver.get("http://siddharth.questionpro.com/")

# Clicked the first Next Button
first_next_button = driver.find_element_by_xpath("//input[@id='SurveySubmitButtonElement']")
first_next_button.click()
print("Clicked the first Next Button")

#On Second Page
print("Now on the Second Page")
id_list = [
	choice(['249227979ID', '249227980ID', '249227981ID']), 	#q1
	choice(['249227983ID', '249227984ID', '249227985ID', '249227986ID']), 	#q2
	choice(['249227988ID', '249227989ID', '249227990ID']),	#q3
	choice(['249227992ID', '249227993ID', '249227994ID', '249227995ID', '249227996ID', '249227997ID']),	#q4
	'249227998ID',	#q5 -- if this is no then the q6 is not displayed
]

for id in id_list:
	x_path = "//input[@id=" + "\'" + id + "\']"
	element_to_find = driver.find_element_by_xpath(x_path)
	element_to_find.click()

next_button = driver.find_element_by_xpath("//input[@id='SurveySubmitButtonElement']")
next_button.click()
print("Now on the Third Page")

#On the Third Page
id_list = [
	choice(['batteryOption_249228000', 'batteryOption_249228001', 'batteryOption_249228002', 'batteryOption_249228003', 'batteryOption_249228004']),	#q6-option-1
	choice(['batteryOption_249228005', 'batteryOption_249228006', 'batteryOption_249228007', 'batteryOption_249228008', 'batteryOption_249228009']),	#q6-option-2
	choice(['batteryOption_249228010', 'batteryOption_249228011', 'batteryOption_249228012', 'batteryOption_249228013', 'batteryOption_249228014']),	#q6-option-3
	choice(['batteryOption_249228015', 'batteryOption_249228016', 'batteryOption_249228017', 'batteryOption_249228018', 'batteryOption_249228019']),	#q6-option-4
	
	choice(['batteryOption_249228020', 'batteryOption_249228021', 'batteryOption_249228022', 'batteryOption_249228023', 'batteryOption_249228024']),	#q7-option-1
	choice(['batteryOption_249228025', 'batteryOption_249228026', 'batteryOption_249228027', 'batteryOption_249228028', 'batteryOption_249228029']),	#q7-option-1
	choice(['batteryOption_249228030', 'batteryOption_249228031', 'batteryOption_249228032', 'batteryOption_249228033', 'batteryOption_249228034']),	#q7-option-1
	choice(['batteryOption_249228035', 'batteryOption_249228036', 'batteryOption_249228037', 'batteryOption_249228038', 'batteryOption_249228039']),	#q7-option-1
	
	choice(['249228040ID', '249228041ID', '249228042ID']),	#q8
	choice(['249228043ID', '249228044ID', '249228045ID']),	#q9
	choice(['249228047ID', '249228048ID']),	#q10
	choice(['249228049ID', '249228050ID', '249228051ID', '249228052ID']), 	#q11
	'249228054ID',	#q12
		
	choice(['249228060ID', '249228061ID']),	#q17
	choice(['249228062ID', '249228063ID', '249228064ID', '249228065ID']),	#q18
]

for id in id_list:
	x_path = "//input[@id=" + "\'" + id + "\']"
	element_to_find = driver.find_element_by_xpath(x_path)
	element_to_find.click()

""" For the user info """
driver.find_element_by_xpath("//input[@id='249228056ID']").send_keys("John")
driver.find_element_by_xpath("//input[@id='249228057ID']").send_keys("Doe")
driver.find_element_by_xpath("//input[@id='249228058ID']").send_keys("9999999999")

next_button = driver.find_element_by_xpath("//input[@id='SurveySubmitButtonElement']")
next_button.click()

print("Done submitting the response") 
# time.sleep(4)
driver.quit()
