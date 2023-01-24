from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import requests

login_caps = {
    "appium:appPackage": "com.raenaapp",
    "appium:appActivity": "com.raenaapp.MainActivity",
    "platformName": "Android",
    "deviceName": "device",
    #"udid": "emulator-5554",
    #"udid": "192.168.8.121:37757",
    "udid": "RR8T704RCKK",
    "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", login_caps)

def get_link():
    driver.implicitly_wait(5)
    driver.find_element(by=AppiumBy.XPATH, value='(//android.view.ViewGroup[@content-desc="share-press"])[2]').click()
    driver.implicitly_wait(5)
    try:
        driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Konfirmasi & Share Produk']").click()
        driver.implicitly_wait(5)
    except:
        pass
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Copy']").click()
    driver.implicitly_wait(5)
    text = driver.get_clipboard_text()
    return text



driver.implicitly_wait(5)
el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"primary-icon-press\"]/android.view.ViewGroup")
el2.click()

driver.implicitly_wait(5)
el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"browse-by-category-press\"]/android.widget.TextView")
el3.click()

driver.implicitly_wait(5)
el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Skincare']")
el4.click()

time.sleep(5)
el5 = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text,'terjual')]")
time.sleep(3)

for i in el5:
    time.sleep(2)
    i.click()
    time.sleep(7)
    print(get_link())
    time.sleep(3)
    driver.back()