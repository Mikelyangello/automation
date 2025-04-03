from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math as m


browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';")
browser.execute_script("alert('Robots at work');")
