import unittest, os
from appium.options.ios import XCUITestOptions
from appium import webdriver
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy


capabilities = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    "appium:deviceName": "iPad mini (6th generation)",
    "appium:bundleId": "com.zhongwu.ZhihuDaily1",
    "appium:udid": "00008110-000859DA3A51401E",
}

appium_server_url = "http://127.0.0.1:4723/wd/hub"


class appiumSimpleTezt(object):
    def setup(self):
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=XCUITestOptions().load_capabilities(caps=capabilities),
        )

    def tearDown(self):
        print("这里已经执行了teardown，然后睡1秒")
        sleep(2)
        print("这里已经睡了1秒了")
        if self.driver:
            self.driver.quit()

    def test_push_view(self):
        next_view_button = self.driver.find_element(
            by=AppiumBy.XPATH,
            value='//XCUIElementTypeStaticText[@name="今日热点"]',
        )
        next_view_button.click()
        print("这里已经执行了点击了一个按钮")
        sleep(2)
        print("这里已经睡了2秒了")

    def test_click_left_button(self):
        left_button = self.driver.find_element(
            by=AppiumBy.XPATH, value='//XCUIElementTypeImage[@name="Home_Image_Mask"]'
        )
        left_button.click()
        print("这里想点击按钮,反正函数已经执行在这里了")
        sleep(5)
        print("5秒睡完了~")


a = appiumSimpleTezt()

if __name__ == "__main__":
    a.setup()
    a.test_push_view()
    a.test_click_left_button()
    a.tearDown()
