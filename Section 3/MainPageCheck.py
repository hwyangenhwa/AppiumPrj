from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

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

mainCallActivity = "com.oliveyoung.presentation.home.MainActivity"
checkActivity = "com.oliveyoung" + driver.current_activity;
assert mainCallActivity == checkActivity

# 선택적 권한 문구 항목
compare_lst = ['사진 카메라 (선택)', '알림 (선택)', '위치 (선택)', '연락처 (선택)']

# 선택적 권한 4가지 확인
permission_lst = driver.find_elements(by=AppiumBy.XPATH,  
                                      value="//android.view.ViewGroup[@resource-id='com.oliveyoung:id/permission_list_cl']/android.widget.ImageView")
assert len(permission_lst) == 4

permission_section = driver.find_elements(by=AppiumBy.XPATH, 
                                          value='//android.view.ViewGroup[@resource-id= "com.oliveyoung:id/permission_list_cl"]/android.widget.TextView[contains(@text, "(선택)")]')

result_permission_lst = [permission.text for permission in permission_section]
assert compare_lst == result_permission_lst

# 확인 버튼 확인
confirm_tv = driver.find_element(by=AppiumBy.ID, 
                                 value="confirm_tv")
confirm_tv.click()

time.sleep(10)

# Update modal 확인
try:
    appUpdate_modal = driver.find_element(by=AppiumBy.ID, 
                                          value="com_braze_inappmessage_modal")
    if appUpdate_modal.is_enabled():
        # Update Pass
        update_pass = driver.find_element(by=AppiumBy.ID, 
                                          value="com_braze_inappmessage_modal_button_dual_one")
        update_pass.click()
        
except Exception:
    print("APP Update Modal is not find..")
    
# 소개 페이지 확인
olive_young_viewPage = driver.find_element(by=AppiumBy.ID, 
                                           value="view_pager")
if olive_young_viewPage.is_displayed():
    assert True
    close_Btn = driver.find_element(by=AppiumBy.ID, 
                                    value="close_iv")
    close_Btn.click()
    
else:
    assert False

time.sleep(10)

contentPage = driver.find_element(by=AppiumBy.ID, value="content")

if contentPage.is_displayed():

    # MainPage 확인
    navigationMenu = driver.find_elements(by=AppiumBy.XPATH, 
                                        value="//android.widget.TabWidget/android.widget.Button")
    print(len(navigationMenu))
    assert len(navigationMenu) == 6

    specialExhibition = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@resource-id='layout']/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View")

    if specialExhibition.is_enabled():
        if specialExhibition.is_dislayed():
            pass
        else:
            assert False

    # quick Menu
    compare_quickMenu = ['W케어 W케어', '건강템찾기 건강템찾기', '라이브 라이브', '선물하기 선물하기', '세일 세일', '맴버십/쿠폰 맴버십/쿠폰']
    compare_bottomMenu = ['매거진', '셔터', '홈', '히스토리', '마이']

    quickMenu = driver.find_elements(by=AppiumBy.XPATH, 
                                    value="//android.widget.ListView/android.view.View")
    assert len(permission_lst) == 7
    result_permission_lst = [quick.get_attribute("content-desc") for quick in quickMenu]
    assert result_permission_lst == compare_quickMenu

    bottomMenu = driver.find_elements(by=AppiumBy.XPATH, 
                                    value="//android.view.ViewGroup[@resource-id='com.oliveyoung:id=constraintLayoutBottomNavigation']//android.widget.TextView")
    assert len(bottomMenu) == 5
    resultbottomMenu = [menu.text for menu in bottomMenu]
    assert compare_bottomMenu == resultbottomMenu
