import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

timer = 53
link = 'put your link here but dont delete these apostrophes'
views = put how much views you want here with no commas or underscores

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for i in range(views):
    driver.get(link)
    print(f"Starting view {i+1} of {views}...")
    time.sleep(timer)
this script was made by xzyba
