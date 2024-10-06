from testpage import OperationsHelper, run_api_tests
import logging, time

#API TESTS

def test_step_API_1(good_word, bad_word):
    logging.info('Test_API_1 Starting')
    run_api_tests.step1(good_word, bad_word)

def test_step_API_2(login, testtext1):
    logging.info('Test_API_2 Starting')
    run_api_tests.step2(login, testtext1)

def test_step_API_3(login, create_post):
    logging.info('Test_API_3 Starting')
    run_api_tests.step3(login, create_post)

#UI TESTS

def test_step_UI_1(choose_browser):
    logging.info('Test_UI_1 Starting')
    testpage = OperationsHelper(choose_browser)
    testpage.go_to_site()
    testpage.enter_login("test_name")
    testpage.enter_pass("test_password")
    testpage.click_login_button()
    assert testpage.get_check_error_text() == "401"
    logging.info('Test_UI_1 Finished')

def test_step_UI_2(choose_browser, data_file):
    logging.info('Test_UI_2 Starting')
    username, password = data_file
    testpage = OperationsHelper(choose_browser)
    testpage.go_to_site()
    testpage.enter_login(username)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.get_check_text() == "Hello, {}".format(username)
    logging.info('Test_UI_2 Finished')

def test_step_UI_3(choose_browser):
    logging.info('Test_UI_2 Starting')
    testpage = OperationsHelper(choose_browser)
    testpage.click_create_post_button()
    testpage.enter_title("new title")
    testpage.click_save_post_button()
    time.sleep(2)
    assert testpage.get_check_post() == "new title"
    logging.info('Test_UI_3 Finished')

def test_step_UI_4(choose_browser):
    logging.info('Test_UI_4 Starting')
    testpage = OperationsHelper(choose_browser)
    testpage.click_home_button()
    time.sleep(2)
    testpage.click_contact_button()
    testpage.enter_name('Test_name_enter')
    testpage.enter_mail('Test_mail_enter@gb.ru')
    testpage.enter_content('Test_content_enter')
    time.sleep(2)
    testpage.click_contact_us_button()
    time.sleep(2)
    assert testpage.get_alert_form() == "Form successfully submitted"
    logging.info('Test_UI_4 Finished')
