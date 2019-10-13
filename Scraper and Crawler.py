from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import logging
import openpyxl
import os


#Check for the directory
os.chdir(r"C:\Users\Pratik\Desktop\Project")

#Logger Syntax
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

#Initialization of ChromeDriver for Selenium testing
chrome_path = r"C:\Users\Pratik\Desktop\Project\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
driver.get("https://www.tripadvisor.in/Hotel_Review-g635747-d477590-Reviews-Keys_Ronil_Resort-Baga_Goa.html")
driver.maximize_window()


logging.info('Executing Main Function to scrape the contents')
