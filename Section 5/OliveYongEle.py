from enum import Enum
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

class oliveEle(Enum):
	permission_lst = (AppiumBy.PATH, "//android.view.ViewGroup[@resource-id='com.oliveyoung:id/permission_list_cl']/android.widget.ImageView")
	permission_chk = (AppiumBy.PATH, '//android.view.ViewGroup[@resource-id= "com.oliveyoung:id/permission_list_cl"]/android.widget.TextView[contains(@text, "(선택)')
	appUpdate_modal  = (AppiumBy.XAPTH, "com_braze_inappmessage_modal_button_dual_one")
	confirm_tv = (AppiumBy.ID, "confirm_tv")
	olive_young_viewPage = (AppiumBy.ID, "view_pager") 
	close_Btn = (AppiumBy.ID, "close_iv")
	navigationMenu = (By.XPATH,, "//div[@role='tablist']/button/span")