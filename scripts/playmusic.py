from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://ca6ssl.rcast.net/radio/63009/")

button = driver.find_element_by_id("rcastplaybutton")
button.click()
