from appium import webdriver

from python_practice.zuo_ye07_appium02.page.basepage1 import BasePage
from python_practice.zuo_ye07_appium02.page.main1 import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps['platformName'] = 'android'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = 'com.tencent.wework'
            caps['appActivity'] = '.launch.LaunchSplashActivity'
            caps['noReset'] = 'true'

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(12)
        else:
            self.driver.launch_app()

        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        # 关闭APP
        self.driver.close_app()
        # 启动APP
        self.driver.launch_app()

    def goto_main_page(self) -> MainPage:
        return MainPage(self.driver)
