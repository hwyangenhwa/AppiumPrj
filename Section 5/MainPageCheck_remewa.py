from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.common.by import By
from OliveYongEle import oliveEle
from desired import AndroidDesired
from server import AppiumServer

driver = webdriver.Remote(AppiumServer.appium_server_url, options=UiAutomator2Options().load_capabilities(AndroidDesired.capabilities))
time.sleep(10)

mainCallActivity = "com.oliveyoung.presentation.home.MainActivity"
checkActivity = "com.oliveyoung" + driver.current_activity;
assert mainCallActivity == checkActivity

# 선택적 권한 문구 항목
compare_lst = ['사진 카메라 (선택)', '알림 (선택)', '위치 (선택)', '연락처 (선택)']

# 선택적 권한 4가지 확인
permission_lst = driver.find_elements(oliveEle.permission_lst)
assert len(permission_lst) == 4

permission_section = driver.find_elements(oliveEle.permission_chk)

result_permission_lst = [permission.text for permission in permission_section]
assert compare_lst == result_permission_lst

# 확인 버튼 확인
confirm_tv = driver.find_element(oliveEle.confirm_tv)
confirm_tv.click()

time.sleep(10)

# Update modal 확인
try:
    appUpdate_modal = driver.find_element(oliveEle.appUpdate_modal)
    
    if appUpdate_modal.is_enabled():
        # Update Pass
        update_pass = driver.find_element(oliveEle.appUpdate_modal)
        update_pass.click()
        
except Exception:
    print("APP Update Modal is not find..")
    
# 소개 페이지 확인
olive_young_viewPage = driver.find_element(oliveEle.olive_young_viewPage)
if olive_young_viewPage.is_displayed():
    assert True
    close_Btn = driver.find_element(oliveEle.close_Btn)
    close_Btn.click()
    
else:
    assert False

time.sleep(10)

# MainPage 확인 (Context WebView 변경)
webview = driver.contexts[1]
app_view = driver.contexts[0]
driver.switch_to.context(webview)

time.sleep(5)
navigationMenu = driver.find_elements(oliveEle.navigationMenu)
assert len(navigationMenu) == 6

driver.switch_to.context(app_view)

