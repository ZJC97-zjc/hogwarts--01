import requests

from python_practice.zuo_ye_09_api_object.base_api_01 import BaseApi


class WeWork(BaseApi):

    def __init__(self, secret):
        self.token = self.get_token(secret)

    def get_token(self, secret):
        # url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "wwdc8bfcb333b2cce3",
            "corpsecret": secret
        }
        req = {
            "method": "GET",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": params
        }
        r = self.send(req)
        print(r.json())
        print(r.json()['access_token'])
        return r.json()['access_token']
