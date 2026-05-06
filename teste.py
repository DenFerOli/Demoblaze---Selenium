from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.demoblaze.com/')

signin_button = driver.find_element(By.ID, 'signin2')
sign_username = driver.find_element(By.ID, 'sign-username')
sign_password = driver.find_element(By.ID, 'sign-password')
signin_button.click()

time.sleep(1)

sign_username.send_keys('qa_tester')
sign_username.send_keys(Keys.TAB)
sign_password.send_keys('!@#teste')

sign_up_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/button[2]')

sign_up_button.click()

time.sleep(5)