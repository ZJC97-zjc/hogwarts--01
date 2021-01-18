from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from python_practice.zuo_ye07_appium02.page.basepage1 import BasePage


class EditPage(BasePage):
    def edit_name(self, name):
        name_ele = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
        self.send_keys(name_ele, name)
        # self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("小熊猫1号")
        return self

    def edit_gender(self, gender):
        # gender = "女"
        # self.driver.find_element_by_xpath("//*[@text='男']").click()
        sleep(2)
        self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
        if gender == "女":
            # self.find_and_click((MobileBy.XPATH,"//*[@text='女']"))
            self.find_and_click((MobileBy.XPATH, "//*[contains(@text,'女')]"))
        else:
            # self.find_and_click((MobileBy.XPATH,"//*[@text='男']"))
            self.find_and_click((MobileBy.XPATH, "//*[contains(@text,'男')]"))
        return self

    def edit_phone(self, phonenum):
        phone_ele = (MobileBy.ID, "com.tencent.wework:id/fuy")
        self.send_keys(phone_ele, phonenum)
        # self.driver.find_element_by_id("com.tencent.wework:id/fuy").send_keys("13000000000")
        return self

    def edit_email(self, email):
        email_ele = (MobileBy.XPATH, "//*[contains(@text,'邮箱')]/../android.widget.EditText")
        self.send_keys(email_ele, email)
        # self.driver.find_element_by_xpath("//*[contains(@text,'邮箱')]/../android.widget.EditText").send_keys("100000000@qq.com")
        return self

    def edit_address(self, address):
        self.find_and_click((MobileBy.XPATH, "//*[contains(@text,'地址')]/../android.widget.RelativeLayout"))
        self.send_keys((MobileBy.ID, "com.tencent.wework:id/js"), address)
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/ie7"))

        # self.driver.find_element_by_xpath("//*[contains(@text,'地址')]/../android.widget.RelativeLayout").click()
        # self.driver.find_element_by_id("com.tencent.wework:id/js").send_keys("幸福小区15栋1单元101室")
        # self.driver.find_element_by_id("com.tencent.wework:id/ie7").click()
        return self

    def edit_apartment(self):
        self.find_and_click(
            (MobileBy.XPATH, "//*[contains(@text,'设置部门') and @resource-id='com.tencent.wework:id/b81']"))
        self.find_and_click((MobileBy.XPATH, "//*[@text='确定(1)']"))

        # self.driver.find_element_by_xpath("//*[contains(@text,'设置部门') and @resource-id='com.tencent.wework:id/b81']").click()
        # self.driver.find_element_by_xpath("//*[@text='确定(1)']").click()
        return self

    def click_save(self):
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/ie7"))
        # self.driver.find_element_by_id("com.tencent.wework:id/ie7").click()
        from python_practice.zuo_ye07_appium02.page.addmemberpage1 import AddmemberPage
        return AddmemberPage(self.driver)
