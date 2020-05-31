

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


https://ui.headspin.io/university/learn/appium-intro/units/sessions







# technical notes
1.) driver.getPageSource()     - Will print the xml tree
2.) content-desc is an alias for accessibilityID for android. In the XML tree, only content-des will
be displayed



