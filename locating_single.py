from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=2AUXV5X8ZBTR&sprefix=laptop%2Caps%2C1123&ref=nb_sb_noss_2")
time.sleep(10)
driver.close()