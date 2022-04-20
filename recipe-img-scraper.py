from selenium import webdriver
url = 'https://www.google.com/search?tbm=isch&q='
DRIVER_PATH = './chromedriver'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# browser = driver.get(url+'Campfire Orange Cake')
# delay = 3 # seconds
# try:
#     myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="islrg"]/div[1]/div[1]')))
#     print("Page is ready!")
# except TimeoutException:
#     print("Not found")
# finally:
#     driver.quit() 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import urllib
import time
start = time.time()
opt = Options()
opt.headless=True
driver = webdriver.Firefox(options=opt)
driver.get(url+'Parfatti pizza')
xpathQuery = '//*[@id="islrg"]/div[1]/div[1]/a[1]'
secQuery = '//*[@id="Sva75c"]/div'
#CLick element first
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, xpathQuery))
    )
    element.click()
    checkEl = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, secQuery))
    )
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, xpathQuery))
    )

    hrefResult = element.get_attribute('href').replace('/imgres?imgurl=', '')
    unquoted = urllib.unquote(hrefResult).decode('utf8').replace('https://www.google.com', '')
    filtered = unquoted.split('&imgrefurl')
    print("filtered "+filtered[0])
    end = time.time()
    dur = end - start
    print("Elapsed: ", dur)
except TimeoutException:
    print("timeout")
except Exception as e:
    print(e)
finally:
    driver.quit()
    exit()