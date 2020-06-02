import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

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
driver.swipe(100, 900, 100, 0)





	//android.view.View[@content-desc="20,512 views"]

likes_container = driver.find_element_by_xpath('//android.view.View')
number_of_likes = likes_container.get_attribute('content-desc')

driver.find_element_by_xpath('//android.view.View')

comments_container = driver.find_elements_by_xpath('//com.instagram.ui.widget.textview.IgTextLayoutView')
comments_container = comments_container[1]
author = comments_container.find_elements_by_xpath('//android.view.View')[0].get_attribute('content-desc')
post_title = comments_container.find_elements_by_xpath('//android.view.View')[1].get_attribute('content-desc')


comments_container = driver.find_element_by_xpath('//com.instagram.ui.widget.textview.IgTextLayoutView')
author = comments_container.find_elements_by_xpath('//android.view.View')[0].get_attribute('content-desc')
post_title = comments_container.find_elements_by_xpath('//android.view.View')[1].get_attribute('content-desc')

# /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/com.instagram.ui.widget.textview.IgTextLayoutView


def scrape_data_and_like_posts(driver):
    for _ in range(20):
        try:
            like_button = driver.find_element_by_accessibility_id('Like')
            if like_button.get_attribute('checked') == 'false':
                like_button.click()
                comments_container = driver.find_element_by_xpath('//com.instagram.ui.widget.textview.IgTextLayoutView')
                author = comments_container.find_elements_by_xpath('//android.view.View')[0].get_attribute('content-desc')
                post_title = comments_container.find_elements_by_xpath('//android.view.View')[1].get_attribute('content-desc')
                print(f"LIKING POST with title {post_title}")
                print(f"AUTHORED by {author}")
            else:
                driver.swipe(100, 900, 100, 0)
        except (NoSuchElementException, IndexError):
            driver.swipe(100, 900, 100, 0)

scrape_data_and_like_posts(driver)

def like_several_posts(driver):
    """ like all of the posts/stories in the first 20 sqipes(approx. 1800 pixels)"""
    for _ in range(20):
        try:
            like_button = driver.find_element_by_accessibility_id('Like')
            if like_button.get_attribute('checked') == 'false':
                like_button.click()
            else:
                driver.swipe(100, 900, 100, 0)
        except NoSuchElementException:
            driver.swipe(100, 900, 100, 0)

like_several_posts(driver)


# Actions are ... weird with mobile webdriver
actions = TouchAction(driver)
actions.press(x=100, y=100)
actions.move_to(x=1000, y=1000)
actions.release()
actions.perform()

scroll_action = TouchAction(driver)
scroll_action.press(x=300, y=900).move_to(x=300, y=400).release().perform()
