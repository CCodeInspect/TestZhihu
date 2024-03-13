# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

options = AppiumOptions()
options.load_capabilities({
	"platformName": "iOS",
	"appium:automationName": "XCUITest",
	"appium:deviceName": "iPad mini (6th generation)",
	"appium:includeSafariInWebviews": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

appium_server_url='http://localhost:4723/wd/hub'

driver = webdriver.Remote(appium_server_url, options=options)
# print(driver)

# e =driver.find_element(by=AppiumBy.XPATH,value='//XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeOther[2]')
# time.sleep(20)



driver.quit()