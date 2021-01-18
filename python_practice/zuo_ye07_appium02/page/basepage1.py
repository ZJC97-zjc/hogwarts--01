from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # 封装 driver初始化
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 封装 find.element
    def find(self, locator):
        return self.driver.find_element(*locator)

    # 封装 find.element().click
    def find_and_click(self, locator):
        self.find(locator).click()

    # 封装滚动查找
    def find_scroll_and_click(self, text):
        ele_scroll = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                    'scrollable(true).instance(0)).'
                                                    'scrollIntoView(new UiSelector().'
                                                    f'text("{text}").instance(0));')
        self.find_and_click(ele_scroll)

    # 封装 toast
    def find_and_get_text(self, locator):
        return self.find(locator).text

    # 封装 send_keys
    def send_keys(self, locator, mess):
        self.find(locator).send_keys(mess)
