import requests

from python_practice.zuo_ye_09_api_object.wework_02 import WeWork


class Tips(WeWork):

    def create_tips(self, tagname, tagid):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {
            "tagname": tagname,
            "tagid": tagid
        }
        req = {
            "method": "POST",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}",
            "json": data
        }
        # r = requests.request(method="POST", url=url, json=data)
        r = self.send(req)
        print(r.json())
        return r.json()

    def updata_tips(self, tagname, tagid):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
            "tagid": tagid,
            "tagname": tagname
        }
        req = {
            "method": "POST",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
            "json": data
        }
        # r = requests.request(method="POST", url=url, json=data)
        r = self.send(req)
        print(r.json())
        return r.json()

    def delete_tips(self, tagid):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        req = {
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        }
        # r = requests.request(method="GET", url=url)
        r = self.send(req)
        print(r.json())
        return r.json()

    def get_tips_member(self, tagid):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}"
        req = {
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}"
        }
        # r = requests.request(method="GET", url=url)
        r = self.send(req)
        print(r.json())
        return r.json()

    def add_tips_member(self):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}"
        data = {
            "tagid": 5,
            # "userlist": ["测试2号"],
            "partylist": [1]
        }
        req = {
            "method": "POST",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}",
            "json": data
        }
        # r = requests.request(method="POST", url=url, json=data)
        r = self.send(req)
        print(r.json())
        return r.json()

    def delete_tips_member(self):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={self.token}"
        data = {
            "tagid": 5,
            # "userlist":[ "user1","user2"],
            "partylist": [1]
        }
        req = {
            "method": "POST",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={self.token}",
            "json": data
        }
        # r = requests.request(method="POST", url=url, json=data)
        r = self.send(req)
        print(r.json())
        return r.json()

    def get_tips_list(self):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        req = {
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        }
        # r = requests.request(method="GET", url=url)
        r = self.send(req)
        print(r.json())
        return r.json()
