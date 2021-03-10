import re
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from services import *

print("Enter the number to be bombarded:")
phoneNumber = input()

# Checking whether 10 digits phone number or not
if not re.match(r"^[0-9]{10}$", phoneNumber):
    print("Enter a valid phone number")
    exit(0)

# Configuring headless mode
options = Options()
options.headless = True

# Location of WebDriver
webdriverLocation = f"{os.getcwd()}/chromedriver"

# Change the path to webdriver if needed
browser = webdriver.Chrome(options=options, executable_path=webdriverLocation)

# Flipkart Bomber
print("Starting Flipkart Bomber")
flipkart.flipkartBomber(browser, phoneNumber)
print("Ending Flipkart Bomber")

# Amazon Bomber
print("Starting Amazon Bomber")
amazon.amazonBomber(browser, phoneNumber)
print("Ending Amazon Bomber")

# Oyo Bomber
print("Starting OYO Bomber")
oyo.oyoBomber(browser, phoneNumber)
print("Ending OYO Bomber")

# Uber Bomber
print("Starting Uber Bomber")
uber.uberBomber(browser, phoneNumber)
print("Ending Uber Bomber")
