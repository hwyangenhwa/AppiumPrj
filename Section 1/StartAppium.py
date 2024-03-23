from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

capabilities = dict(
    platformName= 'Android',
    platformVersion= '14',
    automationName='uiautomator2',
    deviceName='Pixel 3a API',
    appPackage='com.oliveyoung',
    appActivity='com.oliveyoung.presentation.home.MainActivity',
    newCommandTimeout=60
)

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))