import requests
import yaml
from conftest import data
from soap import checkText

with open("config.yaml") as f:
    data = yaml.safe_load(f)

def test_step1(good_word, bad_word):
    assert good_word in checkText(bad_word)

def test_step2(login, testtext1):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", params={"owner": "notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    assert testtext1 in listres

def test_step3(login, create_post):
    post_data = create_post
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", headers=header)
    listres = [i for i in res.json()["data"] if i["description"] == post_data["description"]]
    assert len(listres) > 0, "Post not found on server."
