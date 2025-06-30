from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
query = "laptop"
for i in range (1,20):
    driver.get("https://www.amazon.in/s?k=laptops&crid=2AUXV5X8ZBTR&sprefix=laptop%2Caps%2C1123&ref=nb_sb_noss_2")
    elems = driver.find_element(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} Items Found !!")
    for elem in elems:
        print(elem.text)

time.sleep(10)
driver.close()


