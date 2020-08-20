import pytest
from selenium import webdriver
from utilities.utility import *
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import readConfig
from utilities.nopCommerceLogger import LogGeneration

import time


class Test_0001_Login:
    logger = LogGeneration.loggen()
    baseURL = readConfig.login_page_url()
    email = readConfig.login_email()
    password = readConfig.login_password()
    screen_shots = readConfig.screen_shots()



    def test_homePageTitle(self, setup):
        self.logger.info("RUN Started FOR Test_0001_Login")
        self.logger.info("RUNNING TEST CASE : test_homePageTitle")
        self.logger.info("Verifying home page title")
        #self.driver = webdriver.Chrome("{0}".format(CHROME_DRIVER_PATH))
        self.driver = setup
        self.driver.get(self.baseURL)
        #self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.driver.close()
            self.logger.info("TEST CASE : test_homePageTitle : PASSED")
            assert True
        else:
            self.driver.save_screenshot(self.screen_shots + r"\test_homePageTitle.png")
            self.driver.close()
            self.logger.warning("TEST CASE : test_homePageTitle : FAILED")
            assert False

    def test_login(self, setup):
        #self.driver =webdriver.Chrome("{0}".format(CHROME_DRIVER_PATH))
        self.logger.info("RUNNING TEST CASE : test_login")
        self.logger.info("Verifying User Login")
        self.driver = setup
        self.driver.get(self.baseURL)
        #self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.login_page = LoginPage(self.driver)
        self.login_page.setEmailId(self.email)
        self.login_page.setPassword(self.password)
        time.sleep(4)
        self.login_page.clickOnLogin()
        time.sleep(5)
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("TEST CASE : test_login : PASSED")
            assert True
        else:
            self.driver.save_screenshot(self.screen_shots + r"\test_login.png")
            self.driver.close()
            self.logger.warning("TEST CASE : test_login : FAILED")
            assert False
