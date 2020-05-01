from appium import webdriver


class Driver:

    def __init__(self):

        desired_caps = {    
            'platformName': 'android',
            'deviceName': 'OnePlus 6',
            'appPackage': 'com.oneplus.calculator',
            'appActivity': 'com.oneplus.calculator.Calculator'
        }

        self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)

#######

import unittest

from appium.webdriver.common.mobileby import MobileBy

from webdriver.webdriver import Driver


class CalculatorTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_calculator_launches(self):
        self.driver.instance.find_element(MobileBy.ID, "com.oneplus.calculator:id/digit_8").click()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)