from appium.webdriver.common.mobileby import MobileBy

from python_practice.zuo_ye07_appium02.page.addresspage1 import AddressPage
from python_practice.zuo_ye07_appium02.page.basepage1 import BasePage


class MainPage(BasePage):
    address_element = (MobileBy.XPATH, "//*[contains(@text,'通讯录') and @resource-id='com.tencent.wework:id/elq']")

    def click_address_page(self):
        self.find_and_click(self.address_element)

        return AddressPage(self.driver)
