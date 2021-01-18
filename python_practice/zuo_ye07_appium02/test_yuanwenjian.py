from appium import webdriver


class TestAddMem:
    def setup(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = '127.0.0.1:7555'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        caps['noReset'] = 'true'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(12)

    def teardown(self):
        self.driver.quit()

    def test_add_mem(self):
        # 点击通讯录
        self.driver.find_element_by_xpath(
            "//*[contains(@text,'通讯录') and @resource-id='com.tencent.wework:id/elq']").click()
        # 滚动查找“添加成员”
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        'text("添加成员").instance(0));').click()
        # 点击手动添加成员
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        # 姓名
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("小熊猫1号")
        # 性别
        self.driver.find_element_by_xpath("//*[@text='男']").click()
        self.driver.find_element_by_xpath("//*[@text='女']").click()
        # 电话
        self.driver.find_element_by_id("com.tencent.wework:id/fuy").send_keys("13000000000")
        # 邮箱
        self.driver.find_element_by_xpath("//*[contains(@text,'邮箱')]/../android.widget.EditText").send_keys(
            "100000000@qq.com")
        # 地址
        self.driver.find_element_by_xpath("//*[contains(@text,'地址')]/../android.widget.RelativeLayout").click()
        self.driver.find_element_by_id("com.tencent.wework:id/js").send_keys("幸福小区15栋1单元101室")
        self.driver.find_element_by_id("com.tencent.wework:id/ie7").click()
        # 部门
        self.driver.find_element_by_xpath(
            "//*[contains(@text,'设置部门') and @resource-id='com.tencent.wework:id/b81']").click()
        self.driver.find_element_by_xpath("//*[@text='确定(1)']").click()
        # 点击确定
        self.driver.find_element_by_id("com.tencent.wework:id/ie7").click()
        # 断言：添加成员
        toast_ele = self.driver.find_element_by_xpath("//*[@text='添加成功']").text
        assert toast_ele == "添加成功"
        # 删除
        self.driver.find_element_by_id("com.tencent.wework:id/idp").click()
        self.driver.find_element_by_id("com.tencent.wework:id/ie5").click()
        self.driver.find_element_by_xpath("//*[@text='小熊猫1号']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/eqy").click()
        self.driver.find_element_by_id("com.tencent.wework:id/bom").click()
        # dele_ele = self.driver.find_element_by_xpath("//*[@test='小熊猫1号']").text
        # if "小熊猫1号" == dele_ele:
        #     print("删除失败")
        # else:
        #     print("删除成功")
