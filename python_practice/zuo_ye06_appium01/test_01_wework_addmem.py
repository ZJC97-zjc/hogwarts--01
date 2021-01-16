from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddMember:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(12)

    def teardown(self):
        sleep(4)
        self.driver.quit()

    @pytest.mark.parametrize('name,email', [
        ('小熊猫10号', '10000010@qq.com'),
        ('小熊猫11号', '10000011@qq.com'),
        ('小熊猫12号', '10000012@qq.com'),
        ('小熊猫13号', '10000013@qq.com')
    ])
    def test_add_member(self, name, email):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/csn']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/ern']"
                                          "/android.widget.RelativeLayout/android.widget.EditText").send_keys(name)
        self.driver.find_element_by_id("com.tencent.wework:id/er7").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/boh']"
                                          "/android.widget.RelativeLayout[2]").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/er1']"
                                          "/android.widget.RelativeLayout/android.widget.EditText").send_keys(
            email)  # 输入邮箱
        self.driver.find_element_by_id("com.tencent.wework:id/ie7").click()  # 点击保存
        sleep(1.5)
        # print(self.driver.page_source)
        ele_toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        print(ele_toast)
        assert "添加成功" == ele_toast
