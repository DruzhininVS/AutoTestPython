import pytest, yaml, requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)
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

