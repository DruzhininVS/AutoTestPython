from baseapp import BasePage
from selenium.webdriver.common.by import By
import logging, yaml, requests
from soap import checkText

address = "https://test-stand.gb.ru/"

class run_api_tests:
    def step1(good_word, bad_word):
        try:
            result = checkText(bad_word)
            assert good_word in result, f"'{good_word}' not found in the response from checkText."
            logging.info('Test_API_1 Finished')
        except Exception as e:
            logging.error(f"Error in Test_API_1: {e}")
            raise

    def step2(login, testtext1):
        header = {"X-Auth-Token": login}
        try:
            logging.info("Fetching posts with owner='notMe'")
            res = requests.get(address + "api/posts", params={"owner": "notMe"}, headers=header)
            res.raise_for_status()
            listres = [i["title"] for i in res.json()["data"]]
            assert testtext1 in listres, f"'{testtext1}' not found in post titles: {listres}"
            logging.info('Test_API_2 Finished')
        except requests.RequestException as e:
            logging.error(f"HTTP error in Test_API_2: {e}")
            raise
        except KeyError as e:
            logging.error(f"Key error in Test_API_2: {e}")
            raise

    def step3(login, create_post):
        post_data = create_post
        header = {"X-Auth-Token": login}
        try:
            res = requests.get(address + "api/posts", headers=header)
            res.raise_for_status()
            listres = [i for i in res.json()["data"] if i["description"] == post_data["description"]]
            assert len(listres) > 0, "Post not found on server."
            logging.info('Test_API_3 Finished')
        except requests.RequestException as e:
            logging.exception(f"HTTP error in Test_API_3: {e}")
            raise
        except KeyError as e:
            logging.debug(f"Key error in Test_API_3: {e}")
            raise

class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with{locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Click button {element_name}")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

#Enter TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")
    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")
    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_FIELD"], word, description="title form")
    def enter_name(self,word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_FIELD"], word, description="name form")
    def enter_mail(self,word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_MAIL_FIELD"], word, description="mail form")
    def enter_content(self,word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], word, description="content form")

#CLICK BUTTON
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")
    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="create post")
    def click_home_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_HOME_BTN"], description="home")
    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="contact")
    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="save post")
    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="contact us")

#GET TEXT
    def get_check_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CHECK_ERROR_TEXT"], description="check error text")
    def get_check_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CHECK_LOGIN_FIELD"], description="check login")
    def get_check_post(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CHECK_POST"], description="check post")



