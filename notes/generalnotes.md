
# general notes
0.) Appium server has to be running to run a python module
1.) Android studio doesnt need to be open to run a python module 
2.) AVD(android virtual device) doesnt need to be powered up, Appium server will start deviceName
3.) XPATH locators are not recommended in Mobile Development, just like web development
4.) (EVENTHOUGH) The application is displayed in an XML tree
5.) id != accessibility ID . 
6.) Interesting, Instagram doesnt remember user credentials and auto login when launched with appActivity
7.) emulator vs simulator (apparently android => emulator with avd, ios => simulator)(emulators emulate hardware & software,
simulators simulate just software)
8.) ESPRESSO CAN't BE USED FOR DEVICES THAT YOU DONT OWN/RUN LOCALLY
9.) UIAutomator2 is the industry standard for android automation(owned and maintained by Google)
10.) XML has no predefined tags like HTML does. The XML DOM will not include any display information(colors, sizes, etc.)
11.) All elements in the layout are built using a hierarchy of View and ViewGroup objects
12.) The View objects are usually called "widgets" and can be one of many subclasses, such as Button or TextView. 
13.) The ViewGroup objects are usually called "layouts" can be one of many types that provide a different layout structure, such as LinearLayout or ConstraintLayout . "Viewgroup is the invisible container". We dont want to use them
as elements to find.
14.) The app is "programatically" creating the view/ViewGroup and XML DOM.
15.) Linear Layout VS. Web View(see https://developer.android.com/guide/topics/ui/declaring-layout#CommonLayouts)




# technical notes
1.) `driver.getPageSource()`     - Will print the xml tree
2.) content-desc is an alias for accessibilityID for android.
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

# XML notes
1.) XML trees must have a root node that all other nodes are a descendent of. I see <hierarchy> tag
for android XML DOM
2.) Every XML doc must start with a single line, called the XML Prolog. e.g <?xml version="1.0" encoding="UTF-8"?>
3.) All elements must have a closing tag
4.) XML tags are case sensitive. (unlike HTML tags, which are case insensitive
5.) There are no in-line tags in XML, everything must be properly nested. 
6.) XML elements can have attributes in name/value pairs just like in HTML.
7.) Self closing tags  <android.widget.TextView text='hi' />