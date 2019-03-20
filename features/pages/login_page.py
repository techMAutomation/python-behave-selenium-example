from page_elements import Element, InputField
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser
import logging
import time


class LoginPage(Browser):

    LOGIN_LINK = Element(By.CSS_SELECTOR, 'a.btn.btn-primary.btn-inverse.btn-sm.btn-ajax-login')
    USERNAME_TEXTFIELD = InputField(By.ID, 'username')
    PASSWORD_TEXTFIELD = InputField(By.ID, 'password')
    LOGIN_SUBMIT_BUTTON = Element(By.CSS_SELECTOR, 'button.btn.btn-primary.ajaxLogIn')
    LOGIN_CLOSE_BUTTON = Element(By.XPATH, '//*[@id="ajaxLoginModal"]/div[3]/button[2]')

    JOIN_NOW_LINK = Element(By.CSS_SELECTOR, 'a[href="/register"]')

    def navigate(self, address):
        self.driver.get(address)
        time.sleep(2)

    def click_login_link(self):
        try:
            if (WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'a.btn.btn-primary.btn-inverse.btn-sm.btn-ajax-login')))):
                if self.LOGIN_LINK.text == 'SIGN IN':
                    self.LOGIN_LINK.click()
                    logging.info('- Clicked on Login link -')
        except NoSuchElementException:
            logging.info(' - Element not found and login link test failed -')

    def enter_username(self, username):
        self.USERNAME_TEXTFIELD.send_keys(username)
        logging.info('- Entered Username : %s' % username)

    def enter_password(self, password):
        self.PASSWORD_TEXTFIELD.send_keys(password)
        logging.info('- Entered Password : %s' % password)

    def click_login_page_submit_button(self):
        if self.LOGIN_SUBMIT_BUTTON.text == 'Log-in':
            self.LOGIN_SUBMIT_BUTTON.click()
            logging.info('- Clicked on Login Submit button -')

    def click_login_close_button(self):
        if self.LOGIN_CLOSE_BUTTON.text == 'Close':
            self.LOGIN_CLOSE_BUTTON.click()
            logging.info('- Clicked on Login Close button -')
            time.sleep(2)

    # JOIN NOW Methods

    def click_join_now_link(self):
        try:
            if self.JOIN_NOW_LINK.text == 'JOIN NOW':
                self.JOIN_NOW_LINK.click()
                logging.info('- Clicked on Join Now Link -')
        except NoSuchElementException:
            print(' - Element not found and JoinNow link test failed -')

    def verify_registration_url(self):
        return self.driver.current_url
