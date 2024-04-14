from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.common.by import By

def start_driver():
	capabilities = dict(
    platformName= 'Android',
    platformVersion= '14',
    automationName='uiautomator2',
    deviceName='Pixel 3a API',
    appPackage='com.oliveyoung',
    appActivity='com.oliveyoung.presentation.home.MainActivity',
    newCommandTimeout=60,
    autoGrantPermissions=True,
    noReset=False
	)

	appium_server_url = 'http://localhost:4723'

	driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
	time.sleep(10)
	
	return driver

def wait_element(driver, locator, element):
        
        if locator == 'id':
            time.sleep(5)
            return driver.find_element(By.ID, element)
        
        elif locator == 'classname':
            time.sleep(5)
            return driver.find_elment(By.CLASS_NAMEm, element)
        
        elif locator == 'xpath':
            time.sleep(5)
            return driver.find_element(By.XPATH, element)

def wait_elements(driver, locator, element):
        
        if locator == 'id':
            time.sleep(5)
            return  driver.find_elements(By.ID, element) \
                if len(driver.find_elements(By.ID, element)) > 0 else Exception("Element is not Error")
        
        elif locator == 'classname':
            time.sleep(5)
            return driver.find_elments(By.CLASS_NAME, element) \
                if len(driver.find_elements(By.CLASS_NAME, element)) > 0 else Exception("Element is not Error")
        
        elif locator == 'xpath':
            time.sleep(5)
            return driver.find_elements(By.XPATH, element) \
                if len(driver.find_elements(By.XPATH, element)) > 0 else Exception("Element is not Error")

def click_element(driver, locaotr, elememt):
    time.sleep(5)
    click_element = wait_element(driver, locaotr, elememt)
    click_element.click()

def chageView(driver, view):
    chage_viewOpt = None
    
    if view == 'web':
        chage_viewOpt = driver.contexts[1]
        time.sleep(5)
    else:
        chage_viewOpt = driver.contexts[0]
        time.sleep(5)

    driver.switch_to.context(chage_viewOpt)
    
driver= start_driver()

mainCallActivity = "com.oliveyoung.presentation.home.MainActivity"
checkActivity = "com.oliveyoung" + driver.current_activity;
assert mainCallActivity == checkActivity

# 선택적 권한 문구 항목
compare_lst = ['사진 카메라 (선택)', '알림 (선택)', '위치 (선택)', '연락처 (선택)']

# 선택적 권한 4가지 확인
permission_lst = wait_elements(driver, "xpath","//android.view.ViewGroup[@resource-id='com.oliveyoung:id/permission_list_cl']/android.widget.ImageView")
assert len(permission_lst) == 4

permission_section = wait_elements(driver, "xpath", '//android.view.ViewGroup[@resource-id= "com.oliveyoung:id/permission_list_cl"]/android.widget.TextView[contains(@text, "(선택)")]')
result_permission_lst = [permission.text for permission in permission_section]
assert compare_lst == result_permission_lst

click_element(driver, "id", "confirm_tv")

# Update modal 확인
try:
    appUpdate_modal = wait_element(driver, "id", "com_braze_inappmessage_modal")
    if appUpdate_modal.is_enabled():
        # Update Pass
        update_pass = wait_element(driver, "id", "com_braze_inappmessage_modal_button_dual_one")
        update_pass.click()
        
except Exception:
    print("APP Update Modal is not find..")

# 소개 페이지 확인
olive_young_viewPage = wait_element(driver, "id", "view_pager")
if olive_young_viewPage.is_displayed():
    assert True
    close_Btn = click_element(driver, "id", "close_iv")
    
else:
    assert False

# MainPage 확인 (Context WebView 변경)
chageView(driver, "web")

navigationMenu = wait_elements(driver, "xpath", "//div[@role='tablist']/button/span")
assert len(navigationMenu) == 6

chageView(driver, "app")