import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import secrets


desired_caps = {
    "platformName": "Android",
    "platformVersion": "10.0",
    "deviceName": "determination",
    "avd": "determination",
    "automationName": "UiAutomator2",
    "appPackage": "com.instagram.android",
    "appActivity": ".activity.MainTabActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

login_button = driver.find_element_by_id('com.instagram.android:id/log_in_button')

wait = WebDriverWait(driver, 10)
a = wait.until(EC.invisibility_of_element(login_button))

# FASCINATING. We use the same selenium WebDriverWait class and
# EC(expected condition) LOGIC. Awesome, I now have half my toolkit back and I dont even
# Have to learn anything

username_field.send_keys(username)

password_field = driver.find_element_by_id('com.instagram.android:id/password')
password_field.send_keys(password)

next_button = driver.find_element_by_id('com.instagram.android:id/next_button')
next_button.click()