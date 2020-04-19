from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options, executable_path="/home/ubuntu/settings/geckodriver/geckodriver")
driver.get("http://google.com/")
print(driver.title)
driver.quit()