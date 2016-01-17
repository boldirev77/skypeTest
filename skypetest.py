'''
    File name:
    Author: Aleksander Boldyrev
    Python Version: 3.4
'''

from selenium import webdriver
import unittest
import HTMLTestRunner
import time
import datetime
import sys
import os


class SkypeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        '''descap = dict(DesiredCapabilities.PHANTOMJS)
        descap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (iPad; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 \
            (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        )'''
        #self.driver = webdriver.PhantomJS()

        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()
        cls.driver.get("https://www.skype.com/en/")
        cls.driver.title

        cls.singInbuttonXpath = ".//*[@id='scom']/ul/li[15]/a/span"
        cls.userFieldId = "username"
        cls.passFieldId = "password"
        cls.signmebuttonId = "signIn"

    def test1_openpage(self):
        time.sleep(1)
        logoXpath  = ".//*[@id='scom']/ul/li[1]/a/span"

        #start https://www.skype.com/en/
        #Verify if the Sing In button is present
        self.driver.find_element_by_xpath(logoXpath)
        self.driver.find_element_by_xpath(self.singInbuttonXpath)

    def test2_clickButton(self):
        time.sleep(1)

        #Click on Sign In button
        #Verify if the Username field is present
        #Verify if the Password field is present
        self.driver.find_element_by_xpath(self.singInbuttonXpath).click()
        self.driver.find_element_by_id(self.userFieldId)
        self.driver.find_element_by_id(self.passFieldId)

    def test3_emptySubmit(self):
        time.sleep(1)
        errorXpath = ".//*[@id='container']/div/div/div[1]/div[1]/span"
        engTxt  = "You did not enter your Skype Name."

        #Clear Username field
        #Clear Password field
        #Verify if the ERROR message appears
        #Checke the Text of ERROR message 'You did not enter your Skype Name.'
        self.driver.find_element_by_id(self.userFieldId).clear()
        self.driver.find_element_by_id(self.passFieldId).clear()
        self.driver.find_element_by_id(self.signmebuttonId).click()
        self.driver.find_element_by_xpath(errorXpath)
        assert(self.driver.find_element_by_xpath(errorXpath)).text == engTxt

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':

    user_input = input('Create HTML report yes(y)/no(n) ???  : ').lower()

    if user_input == 'y':
        suite = unittest.TestLoader().loadTestsFromTestCase(SkypeTest)
        unittest.TextTestRunner(verbosity=3)
        with open(time.strftime('%Y-%m-%d_%H_%M') + "_Test_results.html","w") as f:
            runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='Test Report',description='Demo HTMLTestResults')
            runner.run(suite)

    elif user_input == 'n':
        unittest.main(verbosity=3)

    else: sys.stdout.write("! Invalid input ! -  " + user_input)


