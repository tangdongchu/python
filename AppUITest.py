#coding=UTF-8
'''
Create on 2014-12-11
python 2.7 for window
@author: tangdongchu
'''
import os
import time
from selenium import webdriver

#初始化Appium配置
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {}
desired_caps['automationName'] = 'Selendroid'
desired_caps['platformName'] = 'Android'
desired_caps['browserName'] = ''
desired_caps['deviceName'] = '4df72e3d1fbb30af'
desired_caps['platformVersion'] = '4.2.2'
desired_caps['app'] = PATH('D:\Ctrip_V5.10_SIT7_PRODUCT.apk')
desired_caps['appPackage'] = 'ctrip.android.view'
desired_caps['appActivity'] = 'ctrip.android.view.home.CtripSplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#启动APP，休眠5s
time.sleep(5)

#判断是否有升级弹窗
try:
    el=driver.find_element_by_name("以后再说")
except:
    print "没有新版本"
else:
    print "有新版本，点击以后再说"
    el = driver.find_element_by_name("以后再说")
    el.click()
    time.sleep(2)
el = driver.find_element_by_name("我 的")
el.click()
time.sleep(2)

#判断是否登录
try:
    el=driver.find_element_by_name("登录/注册")
except:
    print "用户已登录，执行登录流程"
else:
    print "用户未登录，执行登录流程"
    el = driver.find_element_by_name("登录/注册")
    el.click()
    time.sleep(2)
    #获取输入框，输入账号密码
    textfields = driver.find_elements_by_class_name("textfield")
    textfields[0].send_keys("wwwwww")
    textfields[1].send_keys("www")
        
    driver.find_element_by_class_name("android.widget.Button").click()
    time.sleep(2)        
driver.find_element_by_name("全部订单").click()

#切换到hybrid页面
driver.switchTo().context("WEBVIEW")
el = driver.find_element_by_id("xxxxxxx:id/searchBtn")
el.click()

#截图
driver.get_screenshot_as_file("D:/tt.png")
driver.back()

#切换到native页面
#driver.switchTo().context("NATIVE_APP")
driver.quit()