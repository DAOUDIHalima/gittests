from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# download the chromedriver.exe from https://chromedriver.storage.googleapis.com/index.html?path=106.0.5249.21/

driver = webdriver.Chrome()

# Login
def login():
    login = open('login.txt') # this is your linkedin account login, store in a seperate text file. I recommend creating a fake account so your real one dosen't get flagged or banned
    line = login.readlines()

    email = line[0]
    password = line[1]

    driver.get("https://www.linkedin.com/login")
    
    # Attente jusqu'à ce que le champ d'email soit visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
    eml = driver.find_element(by=By.ID, value="username")
    eml.send_keys(email)

    # Attente jusqu'à ce que le champ de mot de passe soit visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
    passwd = driver.find_element(by=By.ID, value="password")
    passwd.send_keys(password)

    #  # Attente jusqu'à ce que le bouton de connexion soit cliquable
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"organic-div\"]/form/div[3]/button")))
    login_button.click()
