import requests
from bs4 import BeautifulSoup
import selenium  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import re


epslinks = []
fine = []
scrlink = []
title = []
url = "https://animeheaven.ru/detail/black-clover-tv-dub.88765"
fromat = 'mp4'
print(url)
driver = webdriver.Chrome()
driver.get(url)

# Get All episode links
try:
    element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.infoepbox'))
    )
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    animes = soup.findAll('div', attrs={'class':'infoepbox'})
    for anime in animes:
        downloads = anime.find_all('a')
        links = []
        for download in downloads:
            fine.append(download['href'])
            print(fine[0])
            epslinks.append(anime.text)
    print(epslinks)
    print(fine)
finally:
    driver.quit()

# download 
driver = webdriver.Chrome()
driver.get(fine[0])
try:
    element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.jw-video jw-reset'))
    )
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    animes = soup.findAll('video', attrs={'class':'jw-video jw-reset'})
    for anime in animes:
        downloads = anime.find_all('a')
        links = []
        for download in downloads:
            scrlink.append(download['href'])
            title.append(anime.text)
    print("***********************************************************************************************")
    print("***********************************************************************************************")
    print(scrlink)
    print(title)
finally:
    driver.quit()

cleanString = re.sub('\W+','', title[0] )

urllib.request.urlretrieve(scrlink[0], cleanString+fromat) 
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.CLASS, 'infoepbox')))


# browser.implicitly_wait(30)
#Selenium hands the page source to Beautiful Soup

