from baseapp import BasePage
from selenium.webdriver.common.by import By
import logging
class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN =  (By.CSS_SELECTOR, "button")
    LOCATOR_CHECK_ERROR_TEXT = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_CHECK_LOGIN_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CREATE_POST_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_TITLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_SAVE_BTN = (By.CSS_SELECTOR, "button.button.mdc-button.mdc-button--raised.mdc-ripple-upgraded")
    LOCATOR_CHECK_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_HOME_BTN = (By.CSS_SELECTOR, "span.svelte-1rc85o5")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_MAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.CSS_SELECTOR, "button")

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
    def get_check_error_text(self):
        logging.info(f"Check for error text")
        check_error_text = self.find_element(TestSearchLocators.LOCATOR_CHECK_ERROR_TEXT, time=3)
        text = check_error_text.text
        return text
    def get_check_text(self):
        logging.info(f"Compare with  {TestSearchLocators.LOCATOR_CHECK_LOGIN_FIELD[1]}")
        check_text_field = self.find_element(TestSearchLocators.LOCATOR_CHECK_LOGIN_FIELD , time=3)
        text = check_text_field.text
        return text
    def click_create_post_button(self):
        logging.info("Click create post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()
    def enter_title(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_TITLE_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    def click_save_post_button(self):
        logging.info("Click save button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()
    def get_check_post(self):
        logging.info(f"Compare with {TestSearchLocators.LOCATOR_CHECK_POST[1]}")
        check_post_field = self.find_element(TestSearchLocators.LOCATOR_CHECK_POST, time=3)
        text = check_post_field.text
        return text
    def click_home_button(self):
        logging.info("Click home button")
        self.find_element(TestSearchLocators.LOCATOR_HOME_BTN).click()
    def click_contact_button(self):
        logging.info("Click contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()
    def enter_name(self,word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    def enter_mail(self,word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_MAIL_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_MAIL_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    def enter_content(self,word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    def click_contact_us_button(self):
        logging.info("Click contact us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()
