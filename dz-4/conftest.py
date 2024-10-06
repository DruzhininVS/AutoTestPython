import pytest, yaml, requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from mail import send_mail

with open("data.yaml") as f:
    data = yaml.safe_load(f)
browser = data["browser"]
username = data["username"]
password = data["password"]
address = data["address"]

@pytest.fixture()
def good_word():
    return "Привет"
@pytest.fixture()
def bad_word():
    return "Првет"
@pytest.fixture()
def login():
    res1 = requests.post(address + "gateway/login", data={"username": username, "password": password})
    return res1.json()["token"]
@pytest.fixture()
def create_post(login):
    post_data = {
        "title": "Тестовый пост",
        "description": "Описание первого поста",
        "content": "Содержимое тестового поста"
    }
    header = {"X-Auth-Token": login}
    res = requests.post(address + "api/posts", json=post_data, headers=header)
    return post_data
@pytest.fixture()
def testtext1():
    return "Test Post"

@pytest.fixture(scope="session")
def data_file():
    return username, password
@pytest.fixture(scope="session")
def choose_browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# Отключил, так как прикрепил файл mail.py без данных.

#@pytest.fixture(scope='session', autouse=True)
#def send_result_test():
#    yield
#    send_mail()
