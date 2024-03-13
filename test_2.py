import unittest, os
from appium import webdriver
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy



class TestAppiumSimpleTest(unittest.TestCase):
    def setup(self):
        print("准备开始跑脚本了，现在是执行setup")
        app_path = ""
        app = os.path.abspath(app_path)

        self.driver = webdriver.Remote(
            command_executor="http://localhost:4723/wd/hub",
            desired_capabilities={
                "platformName": "iOS",
                "appium:automationName": "XCUITest",
                "appium:deviceName": "iPad mini (6th generation)",
                "appium:bundleId": "com.zhongwu.ZhihuDaily1",
                "appium:udid": "00008110-000859DA3A51401E",
            },
        )

    def test_push_view(self):
        next_view_button = self.driver.find_element(by=AppiumBy.XPATH,value='//XCUIElementTypeStaticText[@name="小事 · 存款到了十万的时候是什么心情？"]')
        next_view_button.click()
        print("这里已经执行了点击了一个按钮")
        sleep(2)
        print("这里已经睡了2秒了")

    def tearDown(self) -> None:
        print("这里已经执行了teardown，然后睡1秒")
        sleep(1)
        print("这里已经睡了1秒了")
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppiumSimpleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
