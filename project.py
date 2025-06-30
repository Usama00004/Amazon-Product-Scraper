from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
query = "laptop"
file = 0 
for i in range (1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=2AUXV5X8ZBTR&sprefix=laptop%2Caps%2C1123&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    for elem in elems:
        data = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w", encoding="utf-8") as f:
            f.write(data)
    file += 1
time.sleep(10)
driver.close()


