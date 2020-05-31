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
    "appActivity": ".activity.MainTabActivity"
}


# "app": "C:\\Users\\mavri\\.android\\avd\\pixeltest.avd\\data\\app\\com.instagram.android-UeP3HAkolbhVSnKGflx7EQ==\\lib\\x86"

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# driver.launch_app()
# driver.page_source
# google_autofill = driver.find_elements_by_id('com.google.android.gms:id/credential_primary_label')

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

def search_for_cats(driver):
    # working, see: https://gyazo.com/295e8ce292c847fef5f4143db8a59987
    search_tab_button = driver.find_element_by_accessibility_id('Search and Explore')
    search_tab_button.click()
    time.sleep(3)

    search_field = driver.find_element_by_id('com.instagram.android:id/action_bar_search_edit_text')
    search_field.click()
    search_field.clear()
    search_field.send_keys('catsofinstragram')
    time.sleep(3)

    second_search_result = driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
        +'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.wid'
        +'get.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.Fr'
        +'ameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.List'
        +'View/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout'
    )
    second_search_result.click()
    time.sleep(3)

    print("found catsofinstagram")




def open_first_story_and_like(driver):
first_story_video_element = driver.find_element_by_id('com.instagram.android:id/video_states')
first_story_video_element.click()  # Double clicking a video/image likes it
first_story_video_element.click()

like_button = driver.find_element_by_accessibility_id('Like')

# Actions are ... weird with mobile webdriver 
actions = TouchAction(driver)
actions.move_to(like_button)
actions.perform()

















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
