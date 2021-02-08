import requests
from jsonpath import jsonpath


class BaseApi:
    def send(self, req):
        return requests.request(**req)

    def json_path_res(self, obj, expr):
        return jsonpath(obj, expr)
