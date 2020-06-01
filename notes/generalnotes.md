
# general notes
0.) Appium server has to be running to run a python module
1.) Android studio doesnt need to be open to run a python module 
2.) AVD(android virtual device) doesnt need to be powered up, Appium server will start deviceName
3.) XPATH locators are not recommended in Mobile Development, just like web development
4.) (EVENTHOUGH) The application is displayed in an XML tree
5.) id != accessibility ID . 
6.) Interesting, Instagram doesnt remember user credentials and auto login when launched with appActivity
7.) emulator vs simulator (apparently android => emulator with avd, ios => simulator)
8.) ESPRESSO CAN't BE USED FOR DEVICES THAT YOU DONT OWN/RUN LOCALLY
9.) UIAutomator2 is the industry standard(owned and maintained by Google)



# technical notes
1.) driver.getPageSource()     - Will print the xml tree
2.) content-desc is an alias for accessibilityID for android. In the XML tree, only content-des will
be displayed
3.) Same EC(expected conditions) from selenium
4.) Same good practices for waits: Explicit waits for everything, implicit and static waits suck
5.) ` assert next_button.is_displayed()` 
6.) https://github.com/aws-samples/aws-device-farm-appium-python-tests-for-android-sample-app/blob/master/tests/tests/login_test.py   Great use of POM(page-object-model) design with appium. Created by Amazon
7.) `driver.swipe(100, 700, 100, 150)` for instead of scrolling. Not sure if better, but it seems to better
mimic user behavior
8.) `self.driver.install_app('/Users/johndoe/path/to/app.apk'); `
9.) `driver.reset()` resets the app
10.) Multitouch actions. Hard press. A lot of mobile(touch screen) only features need to be considered
# driver.launch_app()
# driver.page_source
# FASCINATING. We use the same selenium WebDriverWait class and
# EC(expected condition) LOGIC. Awesome, I now have half my toolkit back and I dont even
# Have to learn anything

