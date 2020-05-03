from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import json
with open('logindetails.json','r') as f:
  config = json.load(f)


PATH = "C:\Program Files (x86)\chromedriver.exe" #location of web driver
driver = webdriver.Chrome(PATH) #selects the web-browser to use

driver.get("https://bildungsportal.sachsen.de/opal/shiblogin?5")

choose_uni = driver.find_element_by_name("wayfselection")
drp = Select(choose_uni)
drp.select_by_value("18")

login_button = driver.find_element_by_name("shibLogin")
login_button.click()

username = driver.find_element_by_id("username")
username.send_keys(config["user"]["name"])

password = driver.find_element_by_id("password")
password.send_keys(config["user"]["pass"])

login = driver.find_element_by_name("_eventId_proceed")
login.click()

accept = driver.find_element_by_name("_eventId_proceed")
accept.click()


try:
  favourites = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id4b"))
  )
  favourites.click()

  show_all = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "alle anzeigen"))
  )
  show_all.click()

except:
  driver.quit()


driver.execute_script("window.open('http://www.cad-lan.mw.tu-dresden.de/sicher_LM/Scripte_traktoren.html');")
