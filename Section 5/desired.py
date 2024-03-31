class AndroidDesired:
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