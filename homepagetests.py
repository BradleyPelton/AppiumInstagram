import time

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

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

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


