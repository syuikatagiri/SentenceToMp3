#cstomp3 Change Sentence to Mp3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
import time
import os

CHROMEDRIVER = "C:\data\etc\chromedriver.exe"
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
browser.get('https://soundoftext.com/')

fileobj = open('sentence.txt', 'r')
textBox = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/form/div[1]/div/textarea')
submit = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/form/div[3]/input')
countLine = 0

while True:
    line = fileobj.readline()
    if line:
     textBox.send_keys(line)
     countLine += 1
     submit.click()
    else:
        break

#ダウンロードボタンが生成されるまで待機
time.sleep(3)

browser.execute_script("window.scrollTo(600, 1500);")
download = browser.find_elements(By.XPATH, "//*[@id='app']/div[4]/div/div[*]/div[2]/a[2]")

for i in range(countLine):
   
    browser.execute_script('arguments[0].click();', download[i])

fileobj.close()

#ダウンロード完了まで待機
time.sleep(5)
