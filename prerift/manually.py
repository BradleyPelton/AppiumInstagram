from appium import webdriver



desired_caps = {
  "platformName": "Android",
  "platformVersion": "10.0",
  "deviceName": "pixeltest",
  "avd": "pixeltest",
  "appPackage": "com.instagram.android"
}





driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)