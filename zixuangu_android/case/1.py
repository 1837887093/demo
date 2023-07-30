from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
from collections.abc import MutableMapping
import time

zxg_data = {
    "platformName": "Android",
    "appium:PlatformVersion": "12",
    "appium:deviceName": "Xiaomi12X",
    "appium:appPackage": "com.tencent.portfolio",
    "appium:appActivity": "com.tencent.portfolio.splash.PrivacyGuideActivity",
    "appium:noReset": "false" #true/false
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", zxg_data)
driver.implicitly_wait(8)

tongyi = driver.find_element(By.ID, "com.tencent.portfolio:id/btn_accept")
tongyi.click()
time.sleep(5)
bodongclose = driver.find_element(By.ID, "com.tencent.portfolio:id/promote_dialog_cancel_btn_topright")
bodongclose.click()

quanbu = driver.find_element(By.ID, "com.tencent.portfolio:id/market_user_header_default")
print("启动成功")

logintips = driver.find_element(By.ID, "com.tencent.portfolio:id/unlogin_tips")
logintips.click()
logintongyi = driver.find_element(By.ID, "com.tencent.portfolio:id/guide_login_checkbox")
logintongyi.click()
wxlogin = driver.find_element(By.ID, "com.tencent.portfolio:id/login_dialog_wx_txt")
wxlogin.click()
userheader = driver.find_element(By.ID, "com.tencent.portfolio:id/market_user_header")
print("登录成功")

# 获取WebDriver的Cookie
cookies = driver.get_cookies()

# 打印Cookie
for cookie in cookies:
    print("Cookie:", cookie)
