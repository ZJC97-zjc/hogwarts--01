import requests
import pytest


class TestWeWorkTips:

    def setup_class(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "wwdc8bfcb333b2cce3",
            "corpsecret": "aYlsfr_mSEELAnHSvtnNrgx9VYiSqh9GAI0nvWp3lrs"
        }
        r = requests.request(method="GET", url=url, params=params)
        print(r.json())
        print(r.json()['access_token'])
        self.token = r.json()['access_token']
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize("tagname,tagid",
                             [("小西瓜3", 3),
                              ("小西瓜4", 4),
                              ("小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜", 5)
                              ])
    def test_create_tips(self, tagname, tagid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {
            "tagname": tagname,
            "tagid": tagid
        }
        r = requests.request(method="POST", url=url, json=data)
        print(r.json())
        if len(tagname) < 32:
            assert r.json()['errmsg'] == 'created'
        else:
            assert r.json()['errcode'] == 40058

    @pytest.mark.parametrize("tagname,tagid", [
        ("小美眉1", 3),
        ("小美眉2", 4),
    ])
    def test_updata_tips(self, tagname, tagid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
            "tagid": tagid,
            "tagname": tagname
        }
        r = requests.request(method="POST", url=url, json=data)
        print(r.json())
        assert r.json()['errmsg'] == 'updated'

    @pytest.mark.parametrize("tagid", [
        3,
        4
    ])
    def test_delete_tips(self, tagid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        r = requests.request(method="GET", url=url)
        print(r.json())
        assert r.json()['errmsg'] == 'deleted'

    @pytest.mark.parametrize("tagid", [
        3,
        4
    ])
    def test_get_tips_member(self, tagid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}"
        r = requests.request(method="GET", url=url)
        print(r.json())
        assert r.json()['errmsg'] == 'ok'

    def test_add_tips_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}"
        data = {
            "tagid": 4,
            # "userlist": ["测试2号"],
            "partylist": [1]
        }
        r = requests.request(method="POST", url=url, json=data)
        print(r.json())
        assert r.json()['errmsg'] == 'ok'

    def test_delete_tips_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={self.token}"
        data = {
            "tagid": 4,
            # "userlist":[ "user1","user2"],
            "partylist": [1]
        }
        r = requests.request(method="POST", url=url, json=data)
        print(r.json())
        assert r.json()['errmsg'] == 'deleted'

    def test_get_tips_list(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        r = requests.request(method="GET", url=url)
        print(r.json())
        assert r.json()['errmsg'] == 'ok'
