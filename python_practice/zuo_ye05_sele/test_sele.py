from time import sleep

import yaml
from selenium import webdriver


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    cook = driver.get_cookies()
    with open("cok.yaml", "w", encoding='utf-8')as f:
        yaml.dump(cook, f)


def test_login():
    driver = webdriver.Chrome()
    driver.get(
        "https://work.weixin.qq.com/wework_admin/loginpage_wx?redirect_uri=https://work.weixin.qq.com/wework_admin/frame")
    driver.implicitly_wait(6)
    with open("cok.yaml", encoding='utf-8')as g:
        yaml_datas = yaml.safe_load(g)
    print(yaml_datas)
    for cookie in yaml_datas:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    sleep(3)
    driver.find_element_by_id("menu_contacts").click()
    sleep(5)
    driver.find_element_by_xpath("//*[@id='js_contacts47']/div/div[2]/div/div[2]/div[3]/div[9]/a[1]").click()
    sleep(3)
    driver.find_element_by_id("username").send_keys("阿熊")
    driver.find_element_by_id("memberAdd_acctid").send_keys("axiong.121")
    driver.find_element_by_id("memberAdd_phone").send_keys("15619007798")
    driver.find_element_by_xpath("//*[@id='js_contacts47']/div/div[2]/div/div[4]/div/form/div[1]/a[2]").click()
