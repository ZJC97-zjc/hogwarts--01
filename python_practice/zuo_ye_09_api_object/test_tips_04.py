import pytest
import requests
import yaml
import json
from jsonpath import jsonpath

from python_practice.zuo_ye_09_api_object.tips_03 import Tips


class TestTips:

    def setup_class(self):
        conf = yaml.load(open("conf.yaml"))
        secret = conf['tips_secret']
        self.tips = Tips(secret=secret)

    # ***1.添加标签 ***
    @pytest.mark.parametrize("tagname,tagid",
                             [("小西瓜2", 2),
                              ("小西瓜3", 3),
                              ("小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜小西瓜", 5)
                              ])
    def test_create_tips(self, tagname, tagid):
        r = self.tips.create_tips(tagname, tagid)
        r2 = self.tips.get_tips_list()
        print(r2)
        # tips_tagname = jsonpath(r2,"$..taglist[?(@.tagid==7)].tagname")[0]
        tips_tagname = self.tips.json_path_res(r2, "$..taglist[?(@.tagid==2)].tagname")[0]
        print(tips_tagname)
        if len(tagname) < 32:
            assert r['errmsg'] == 'created'
            assert tips_tagname == '小西瓜2'
        else:
            assert r['errcode'] == 40058

    # ***2.更新标签 ***
    @pytest.mark.parametrize("tagname,tagid", [
        ("小老虎0", 2),
        ("小老虎00", 3),
    ])
    def test_updata_tips(self, tagname, tagid):
        r = self.tips.updata_tips(tagname, tagid)
        r2 = self.tips.get_tips_list()
        # print(r2)
        print(json.dumps(r2, ensure_ascii=False))
        # name_list = jsonpath(r2, "$..tagname")
        name_list = self.tips.json_path_res(r2, "$..tagname")
        print(name_list)
        # tips_name = jsonpath(r2, "$..taglist[?(@.tagid==5)].tagname")[0]
        tips_name = self.tips.json_path_res(r2, "$..taglist[?(@.tagid==5)].tagname")[0]
        print(tips_name)
        # 断言 tagname是否在列表中
        assert '小老虎0' in name_list
        # 断言 将制定 tagid 中名称是否更改成功
        assert tips_name == '小老虎0'

        # assert r['errmsg'] == 'updated'
        # assert r2['taglist'][1]['tagname'] == '小美眉00'

    # ***3.删除标签 ***
    @pytest.mark.parametrize("tagid", [
        2,
        3
    ])
    def test_delete_tips(self, tagid):
        r = self.tips.delete_tips(tagid)
        r2 = self.tips.get_tips_list()
        print(r2)
        delete_tips = self.tips.json_path_res(r2, "$..taglist[?(@.tagid==2)].tagname")
        print(delete_tips)
        assert r['errmsg'] == 'deleted'
        assert delete_tips == False

    # ***4.获取标签成员 ***
    @pytest.mark.parametrize("tagid", [
        5,
        6
    ])
    def test_get_tips_member(self, tagid):
        r = self.tips.get_tips_member(tagid)
        assert r['errmsg'] == 'ok'

    # ***5.增加标签成员 ***
    def test_add_tips_member(self):
        r = self.tips.add_tips_member()
        assert r['errmsg'] == 'ok'

    # ***6.删除标签成员 ***
    def test_delete_tips_member(self):
        r = self.tips.delete_tips_member()
        assert r['errmsg'] == 'deleted'

    # ***7.获取标签列表***
    def test_get_tips_list(self):
        r = self.tips.get_tips_list()
        assert r['errmsg'] == 'ok'
