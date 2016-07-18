from selenium import webdriver
import time

def com_reg():
	msg = "My order was marked for return on July 1, and was picked from my residence on July 2. Since that day I have made numerous calls and emails to myntra.com to know more about the return request but was only told to wait a few more days. My registered complaint id is 160705-004212. Please tell when I will get the refund process completed. Such attitude is purely unprofessional and calls for amends. You are making a fool out the customer."

	driver = webdriver.PhantomJS() #getting to start the PhantomJS header webdriver using selenium
	# driver.set_window_size(1120, 550)
	driver.get("https://secure.myntra.com/login?referer=http%3A%2F%2Fwww.myntra.com%2Fcontactus")

	driver.find_element_by_xpath("//input[@type='email']").send_keys("gupta.chetan1997@gmail.com")
	driver.find_element_by_xpath("//input[@type='password']").send_keys("@cafeKAka")
	driver.find_element_by_xpath("//button[@class='login-login-button']").click()
	print "Logged in"
	time.sleep(3)
	driver.find_element_by_xpath("//li[@id='returnexchange']").click()
	driver.find_element_by_xpath("//li[@id='refundnotreceivedreturnpicked']").click()
	driver.find_element_by_xpath("//input[@name='select-order-field']").click()
	print "Order selected"
	time.sleep(3)
	driver.find_element_by_xpath("//div[@class='list-row order']").click()
	time.sleep(3)
	driver.find_element_by_xpath("//button[@type='button']").click()
	time.sleep(3)
	# driver.find_element_by_tag_name('textarea')
	driver.find_element_by_name('notes').send_keys(msg)
	# driver.find_element_by_xpath("//textarea").send_keys(msg)
	driver.find_element_by_xpath("//button[@type='button']").click()
	print "Complaint registered"
	time.sleep(2)
	driver.quit()

def main():
	for i in range(1,50):
		print "Complaint #" + str(i)
		try :
			com_reg()
		except:
			print "Little Fuck Ups"
		print

if __name__ == '__main__':
	main()