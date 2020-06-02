import time
import unittest

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

import secrets


desired_caps = {
    "platformName": "Android",
    "platformVersion": "10.0",
    "deviceName": "determination",
    "avd": "determination",
    "automationName": "UiAutomator2",
    "appPackage": "com.instagram.android",
    "appActivity": ".activity.MainTabActivity",
    "newCommandTimeout": "600"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


def standard_login(driver, username, password):
    # working, see demo : https://gyazo.com/a77bc3787623eeb9890a840612c26a2a
    login_button = driver.find_element_by_id('com.instagram.android:id/log_in_button')
    login_button.click()
    time.sleep(5)

    username_field = driver.find_element_by_id('com.instagram.android:id/login_username')
    username_field.send_keys(username)

    password_field = driver.find_element_by_id('com.instagram.android:id/password')
    password_field.send_keys(password)

    next_button = driver.find_element_by_id('com.instagram.android:id/next_button')
    next_button.click()


standard_login(driver, secrets.INSTA_EMAIL, secrets.INSTA_PASSWORD)

# assert "home page" in driver.page_source, "standard_login failed"
