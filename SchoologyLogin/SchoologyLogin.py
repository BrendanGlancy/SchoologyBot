from selenium import webdriver
import time

# this program logs into schooology for you, because my school made it a pain in the ass
 
username = # enter you gmail here
password = # enter your password here

def login(username, password):
	driver = webdriver.Chrome()
	driver.get('https://app.schoology.com/login?destination=support_auth%3Fbrand_id%3D2854896%26locale_id%3D1%26return_to%3Dhttps%253A%252F%252Fsupport.schoology.com%252Fhc%252Fen-us%252Farticles%252F201001193-Login-Student-%26timestamp%3D1585688988')
	EmailBox = driver.find_element_by_xpath('//*[@id="edit-mail"]')
	EmailBox.send_keys(username)
	PassBox = driver.find_element_by_xpath('//*[@id="edit-pass"]')
	PassBox.send_keys(password)

	LoginButton = driver.find_element_by_xpath('//*[@id="edit-submit"]')
	LoginButton.click()

	Connectlink = driver.find_element_by_xpath('//*[@id="login-container"]/div[1]/div/div/table/tbody/tr/td[2]/div/a')
	Connectlink.click()

	time.sleep(2)
	ConnectPageEmail = driver.find_element_by_xpath('//*[@id="identifierId"]')
	ConnectPageEmail.send_keys('200610@northcantonschools.org')
	NextButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
	NextButton.click()

	time.sleep(2)
	ConnectPagePassword = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
	ConnectPagePassword.send_keys('Yes0Bid1')
	ConnectPageNextButton = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
	ConnectPageNextButton.click()

def physics():
    time.sleep(3)
    driver.get('https://connect.northcantonschools.org/course/2149080707/materials')
def pysch():
    time.sleep(3)
    driver.get('https://connect.northcantonschools.org/course/2149080251/materials')

def programming():
    time.sleep(2)
    driver.get('https://connect.northcantonschools.org/course/2149080270/materials')

pysch()