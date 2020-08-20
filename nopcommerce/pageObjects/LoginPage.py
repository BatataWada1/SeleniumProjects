from utilities.utility import *
from selenium import webdriver
import time

#driver = webdriver.Chrome('{0}'.format(CHROME_DRIVER_PATH))

class LoginPage:

    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    button_logout_xpath ="//a[contains(@href, '/logout')]"

    def __init__(self, driver):
        self.driver = driver

    def setEmailId(self, useremail):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(useremail)

    def setPassword(self, userpassword):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(userpassword)

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickOnLogOut(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()