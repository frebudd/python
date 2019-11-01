from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile" cmd 命令
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
# print(driver.title)
print(driver.get_cookies())
time.sleep(60)
print(driver.get_cookies())
