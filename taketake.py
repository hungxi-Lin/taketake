from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
driver = webdriver.Edge()
 
driver.get('https://webapss.ncue.edu.tw/student/baseuser/loginsso?ref=1')
userid = driver.find_element(By.NAME, "Ecom_User_ID")
Password = driver.find_element(By.NAME, "Ecom_Password")
confirm = driver.find_element(By.NAME, "LoginButton")
userid.send_keys("S1153036")
Password.send_keys("k02-oAE-ajy-PB7")
confirm.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "divContent"))
)



driver.get('https://webapss.ncue.edu.tw/Student/SC020/CodeAD?ControlName=SC020&ActionName=Announce') #代碼選課
lessid1 = driver.find_element(By.NAME, "SCR_SELCODE1")
lessid1.send_keys("00174")
ADD1 = driver.find_element(By.ID, "btnAdd")
ADD1.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[3]/div/div/div/div[2]/div"))
)

########################################################SAFE

ADDcmd = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[3]/div/div/div/div[2]/form/div/table/tbody/tr[6]/td/button[1]")
ADDcmd.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "QueryAddMsg"))
)




#Leave = driver.find_element(By.CSS_SELECTOR, "QueryAddMsg > div > div > div.bg-warning > form > div > table > tbody > tr:nth-child(6) > td > button")
#Leave.send_keys(Keys.RETURN)


#QueryAddMsg > div > div > div.bg-warning > form > div > table > tbody > tr:nth-child(6) > td > button


sleep(30)
driver.close()