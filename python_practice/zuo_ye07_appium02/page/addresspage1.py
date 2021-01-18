from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from python_practice.zuo_ye07_appium02.page.addmemberpage1 import AddmemberPage
from test_04_appium.test_13_zhiboke02.page.base_page import BasePage


class AddressPage(BasePage):
    def click_addmember_page(self):
        self.find_by_scroll_and_click("添加成员")
        return AddmemberPage(self.driver)

    def delet(self):
        sleep(2)
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/ie5"))
        self.find_and_click((MobileBy.XPATH, "//*[@text='小熊猫1号']"))
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/eqy"))
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/bom"))

        # self.driver.find_element_by_id("com.tencent.wework:id/ie5").click()
        # self.driver.find_element_by_xpath("//*[@text='小熊猫1号']").click()
        # self.driver.find_element_by_id("com.tencent.wework:id/eqy").click()
        # self.driver.find_element_by_id("com.tencent.wework:id/bom").click()
