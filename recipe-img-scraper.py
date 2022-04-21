from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import urllib
import time

url = 'https://www.google.com/search?tbm=isch&q='
DRIVER_PATH = './chromedriver'
opt = Options()
opt.headless=True

def scrape_img(keyword):
    driver = webdriver.Firefox(options=opt)
    driver.get(url+keyword)
    cssQuery = '#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy'
    cssSecQuery = '#Sva75c > div'
                
    #CLick element first
    filtered = ''
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, cssQuery))
        )
        element.click()

        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, cssSecQuery))
        )
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, cssQuery))
        )

        hrefResult = element.get_attribute('href').replace('/imgres?imgurl=', '')
        unquoted = urllib.unquote(hrefResult).decode('utf8').replace('https://www.google.com', '')
        filtered = unquoted.split('&imgrefurl')[0]
        
    except TimeoutException:
        print("timeout")
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        return filtered

def scrape_func(row):
    row['image'] = scrape_img(row['name'])
    return row


import dask.dataframe as dd
from dask.diagnostics import ProgressBar
import pandas as pd

ProgressBar().register()
df = pd.read_csv('./100k_preprocessed_recipes.csv')[:500]
ddf = dd.from_pandas(df, npartitions=10) # find your own number of partitions
ddf_update = ddf.apply(scrape_func, axis=1).compute()
ddf_update.to_csv('../datasets/recipes_with_img.csv', index=False)