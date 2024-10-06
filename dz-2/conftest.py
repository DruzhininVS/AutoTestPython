import pytest
import yaml
with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    username = testdata["username"]
    password = testdata["password"]

post_title = "Новый пост"

@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""
@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""
@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""
@pytest.fixture()
def btn_selector1():
    return "button"
@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""
@pytest.fixture()
def er2():
    return "Hello, {}".format(username)
@pytest.fixture()
def er1():
    return "401"
@pytest.fixture()
def btn_selector2():
    return "button"
@pytest.fixture()
def post_title_selector():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
@pytest.fixture()
def create_post_btn_selector():
    return 'button.button.mdc-button.mdc-button--raised.mdc-ripple-upgraded'
@pytest.fixture()
def post_check_selector():
    return """//*[@id="app"]/main/div/div[1]/h1"""
@pytest.fixture()
def er3():
    return "{}".format(post_title)