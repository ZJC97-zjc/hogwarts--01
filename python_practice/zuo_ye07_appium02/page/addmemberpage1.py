from appium.webdriver.common.mobileby import MobileBy

from python_practice.zuo_ye07_appium02.page.basepage1 import BasePage
from python_practice.zuo_ye07_appium02.page.editpage1 import EditPage


class AddmemberPage(BasePage):
    addmem_ele = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def click_to_edit(self):
        # self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.find_and_click(self.addmem_ele)
        return EditPage(self.driver)

    def got_toast(self):
        # toast_ele = self.driver.find_element_by_xpath("//*[@text='添加成功']").text
        toast0 = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        toast_ele = self.find_and_get_text(toast0)

        return toast_ele

    def back_to_delet(self):
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/idp"))
        # self.driver.find_element_by_id("com.tencent.wework:id/idp").click()
        from python_practice.zuo_ye07_appium02.page.addresspage1 import AddressPage
        return AddressPage(self.driver)
