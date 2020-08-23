import shelve
from time import sleep

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestWorkweixin():
    def setup_method(self, method):
        # 复用浏览器
        # option = Options()
        # option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_contact(self):
        sleep(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, "menu_contacts").click()
        # 断言
        myclass = self.driver.find_element(By.ID, "menu_contacts").get_attribute("class")
        # print("myclass")
        assert 'frame_nav_item frame_nav_item_Curr' == myclass

    def test_cookies(self):
        sleep(3)
        cookies = self.driver.get_cookies()
        print(cookies)
