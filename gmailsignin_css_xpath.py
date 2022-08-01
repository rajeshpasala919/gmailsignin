
from selenium import webdriver

from selenium.webdriver.common.by import By

import pdb

driver =webdriver.Chrome()
driver.get('http://www.google.com')
gmail = driver.find_element(By.CSS_SELECTOR, '#gb > div > div:nth-child(1) > div > div:nth-child(1) > a')
gmail.click()

driver.implicitly_wait(5)

driver.get("https://accounts.google.com/signin")
email_or_phone = driver.find_element(By.CSS_SELECTOR, '#identifierId')
email_or_phone.send_keys("rajeshpasalad1@gmail.com")

#password_elem = driver.find_element(By.CSS_SELECTOR,'#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
#password_elem.send_keys("123456")
pdb.set_trace()