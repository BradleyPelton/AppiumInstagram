import time
import unittest

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

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


# "app": "C:\\Users\\mavri\\.android\\avd\\pixeltest.avd\\data\\app\\com.instagram.android-UeP3HAkolbhVSnKGflx7EQ==\\lib\\x86"

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# driver.launch_app()

google_autofill = driver.find_elements_by_id('com.google.android.gms:id/credential_primary_label')

login_button = driver.find_element_by_id('com.instagram.android:id/log_in_button')
# login_button = driver.find_element_by_xpath(
#     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]'
# )
login_button.click()
time.sleep(5)


















email_tab_button = driver.find_element_by_accessibility_id('Email')
# email_tab_button = driver.find_element_by_id('com.instagram.android:id/right_tab')
# email_tab_button = driver.find_element_by_xpath(
#     '//android.widget.LinearLayout[@content-desc="Email"]'
# )
email_tab_button.click()
time.sleep(5)

email_field = driver.find_elements_by_id('com.instagram.android:id/email_field')
email_field.send_keys(secrets.INSTA_EMAIL)
time.sleep(5)

next_button = driver.find_elements_by_id('com.instagram.android:id/button_text')
next_button.click()
time.sleep(5)
