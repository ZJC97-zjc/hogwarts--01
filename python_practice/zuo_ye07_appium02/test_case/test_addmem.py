import pytest
import yaml
from appium import webdriver

from python_practice.zuo_ye07_appium02.page.app1 import App


def get_data():
    with open("data_add.yaml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        addnumber = data['add']
        return addnumber


class TestAddMem:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        self.app.stop()

    # @pytest.mark.parametrize("name,gender,phonenum,email,address",[
    #     ("小熊猫1号","男","13000000001","100000001@qq.com","幸福小区15栋1单元101室"),
    #     ("小熊猫2号","女","13000000002","100000002@qq.com","幸福小区15栋1单元102室")
    # ])
    @pytest.mark.parametrize("name,gender,phonenum,email,address", get_data())
    def test_add_member(self, name, gender, phonenum, email, address):
        toast1 = self.main.click_address_page().click_addmember_page().click_to_edit(). \
            edit_name(name).edit_gender(gender).edit_phone(phonenum).edit_email(email).edit_address(
            address).edit_apartment().click_save()

        toast2 = toast1.got_toast()
        assert toast2 == "添加成功"
        toast1.back_to_delet().delet()
