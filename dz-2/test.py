import yaml
import time
from module import Site
from conftest import post_title

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])
username = testdata["username"]
password = testdata["password"]

def test_step1(x_selector1, x_selector2, btn_selector1, x_selector3, er1):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys('username')
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys('password')
    btn1 = site.find_element("css", btn_selector1)
    btn1.click()
    time.sleep(1)
    user_label = site.find_element("xpath", x_selector3)
    text = user_label.text
    assert text == er1

def test_step2(x_selector1, x_selector2, x_selector4, btn_selector1, er2):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(username)
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(password)
    btn1 = site.find_element("css", btn_selector1)
    btn1.click()
    time.sleep(1)
    user_label = site.find_element("xpath", x_selector4)
    text1 = user_label.text
    assert text1 == er2

def test_step3(btn_selector2, post_title_selector, create_post_btn_selector, post_check_selector, er3):
    btn2 = site.find_element("css", btn_selector2)
    btn2.click()
    time.sleep(2)
    title_input = site.find_element("xpath", post_title_selector)
    title_input.send_keys(post_title)
    create_post_btn = site.find_element("css", create_post_btn_selector)
    create_post_btn.click()
    time.sleep(2)
    check_post = site.find_element("xpath", post_check_selector)
    text2 = check_post.text
    assert text2 == er3
    site.close()
