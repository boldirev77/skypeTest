from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import HTMLTestRunner
import time


class skypetest(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome()
        descap = dict(DesiredCapabilities.PHANTOMJS)
        descap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (iPad; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 \
            (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        )
        self.driver = webdriver.PhantomJS()

        self.driver.implicitly_wait(15)
        self.base_url = "https://www.skype.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.singInbuttonXpath = ".//*[@id='scom']/ul/li[14]/a/span"
        self.logoXpath  = ".//*[@id='scom']/ul/li[1]/a/span"
        self.userFieldId = "username"
        self.passFieldId = "password"
        self.signmebuttonId = "signIn"

    def test1_openpage(self):
        time.sleep(1)
        driver = self.driver
        driver.get(self.base_url + "/en/")
        driver.set_window_size(800, 600)

        #start https://www.skype.com/en/
        #Verify if the Sing In button is present

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(self.singInbuttonXpath))
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(self.logoXpath))
        driver.close()

    def test2_clickButton(self):
        time.sleep(1)
        driver = self.driver
        driver.get(self.base_url + "/en/")
        driver.set_window_size(800, 600)

        #start https://www.skype.com/en/
        #Verify if the Sing In button is present
        #Click on Sign In button
        #Verify if the Username field is present
        #Verify if the Password field is present

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(self.singInbuttonXpath))
        driver.find_element_by_xpath(self.singInbuttonXpath).click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(self.userFieldId))
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(self.passFieldId))
        driver.close()

    def test3_emptySubmit(self):
        time.sleep(1)
        driver = self.driver
        errorXpath = ".//*[@id='content']/div[1]"
        engTxt  = "You did not enter your Skype Name."
        driver.get(self.base_url + "/en/")
        driver.set_window_size(800, 600)

        #start https://www.skype.com/en/
        #Verify if the Sing In button is present
        #Click on Sign In button
        #Verify if the Username field is present
        #Verify if the Password field is present
        #Clear Username field
        #Clear Password field
        #Verify if the ERROR message appears
        #Checke the Text of ERROR message 'You did not enter your Skype Name.'

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(self.singInbuttonXpath))
        driver.find_element_by_xpath(self.singInbuttonXpath).click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(self.signmebuttonId))
        driver.find_element_by_id(self.userFieldId).clear()
        driver.find_element_by_id(self.passFieldId).clear()
        driver.find_element_by_id(self.signmebuttonId).click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(errorXpath))
        assert(driver.find_element_by_xpath(errorXpath)).text == engTxt
        driver.close()


    def tearDown(self):
        self.driver.quit()


# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(skypetest)
#     unittest.TextTestRunner(verbosity=0).run(suite)

if __name__ == "__main__":
    HTMLTestRunner.main()