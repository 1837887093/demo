#自动多轮投简历
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time

boss_data = {
    "platformName": "Android",
    "appium:PlatformVersion": "12",
    "appium:deviceName": "Xiaomi12X",
    "appium:appPackage": "com.hpbr.bosszhipin",
    "appium:appActivity": "com.hpbr.bosszhipin.module.launcher.WelcomeActivity",
    "appium:noReset": "true", #true/false
    "automationName": "uiautomator2"
}
#手机数据

class boss_demo1(unittest.TestCase):
    def test_boss_demo1(self):
        try:
            driver = webdriver.Remote("http://127.0.0.1:4723", boss_data)
            #启动app
            driver.implicitly_wait(10)
            #设置隐式等待10秒
            time.sleep(5)
            #启动app需要时间，等待五秒

            search = driver.find_elements(By.ID, "com.hpbr.bosszhipin:id/img_icon")[1]
            search.click()
            #点击首页右上角的搜索按钮

            et_search = driver.find_element(By.ID, "com.hpbr.bosszhipin:id/et_search")
            et_search.send_keys("软件测试")
            #定位搜索框，输入软件测试
            tv_search = driver.find_element(By.ID, "com.hpbr.bosszhipin:id/tv_search")
            tv_search.click()
            #点击搜索框右侧搜索按钮
            time.sleep(3)
            #搜索结果出现需要时间，强制等待三秒
            tv_tab_label = driver.find_elements(By.ID, "com.hpbr.bosszhipin:id/tv_tab_label")[5]
            tv_tab_label.click()
            #点击筛选按钮
            Education = driver.find_elements(By.ID, "com.hpbr.bosszhipin:id/keywords_view_text")[4]
            Education.click()
            #点击学历限制大专
            Wages =   driver.find_elements(By.ID, "com.hpbr.bosszhipin:id/keywords_view_text")[12]
            Wages.click()
            #点击薪资要求10-20K
            btn_confirm = driver.find_element(By.ID, "com.hpbr.bosszhipin:id/btn_confirm")
            btn_confirm.click()
            #点击完成

            for n in range(10):
                #重复执行10次
                for i in range (0,3):
                    #重复执行三次
                    tv_distance = driver.find_elements(By.ID,"com.hpbr.bosszhipin:id/tv_distance")[i]
                    #定位公司位置
                    distance = tv_distance.text
                    #提取位置地址
                    tv_company_name = driver.find_elements(By.ID,"com.hpbr.bosszhipin:id/tv_company_name")[i]
                    #定位公司名
                    company = tv_company_name.text
                    #提取公司名
                    tv_position_name = driver.find_elements(By.ID, "com.hpbr.bosszhipin:id/tv_position_name")[i]
                    # 定位岗位名称
                    position = tv_position_name.text
                    # 提取岗位名称
                    tv_salary_statue = driver.find_elements(By.ID, "com.hpbr.bosszhipin:id/tv_salary_statue")[i]
                    # 定位薪资范围
                    salary = tv_salary_statue.text
                    # 提取薪资范围
                    print("投递地址是：", distance,company,"岗位名称是：",position,"薪资范围是：",salary)

                    if "龙岗" in distance or "龙华" in distance or "罗湖" in distance or "机场" in distance or "盐田" in distance:
                        #筛选位置关键词，属于以上的都不投递
                        print(distance,"不在范围，不投递")
                        iv_improper = driver.find_elements(By.ID, "com.hpbr.bosszhipin:id/iv_improper")[i]
                        iv_improper.click()
                        #关闭位置不符合要求的公司
                        mtv_reasondesc = driver.find_elements(By.ID, "com.hpbr.bosszhipin:id/mtv_reasondesc")[5]
                        mtv_reasondesc.click()
                        print("位置不符合要求，已关闭并反馈平台：距离过远")
                        # 反馈距离过远
                        break

                    else:
                        if "测试" not in position:
                            print(position,"这不是测试岗，不投递")
                            break
                        else:
                            tv_distance.click()
                        #位置符合要求则点击
                    btn_chat = driver.find_element(By.ID, "com.hpbr.bosszhipin:id/btn_chat")
                    btn_chat.click()
                    #点击立即沟通按钮
                    tv_user_info =  driver.find_element(By.ID, "com.hpbr.bosszhipin:id/tv_user_info")
                    name = tv_user_info.text
                    #定位公司名，提取hr名称
                    now = time.strftime("%H.%M")
                    EditText = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
                    EditText.send_keys("尊敬的",company,name[0].strip(), "先生/女士，您好，此招呼是我用自动化代码在",now,"发送的，请问能了解下我的在线简历，给次面试机会吗")
                    print("已和",company,name,"沟通",position)
                    # 定位聊天框并输入搭配好的文案
                    send = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView")
                    send.click()
                    #点击发送
                    iv_back = driver.find_element(By.ID, "com.hpbr.bosszhipin:id/iv_back")
                    iv_back = driver.find_element(By.ID, "com.hpbr.bosszhipin:id/iv_back")
                    iv_back.click()
                    time.sleep(2)
                    # 点击左上角返回按钮，因为经常定位不到，所以定位两次，并等待两秒
                    iv_back = driver.find_element(By.ID, "com.hpbr.bosszhipin:id/iv_back")
                    iv_back = driver.find_element(By.ID, "com.hpbr.bosszhipin:id/iv_back")
                    iv_back.click()
                    # 点击左上角返回按钮，因为经常定位不到，所以定位两次
                et_search = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")
                et_search.send_keys("软件测试")
                    #定位输入框，输入搜索内容
                tv_search = driver.find_element(By.ID, "com.hpbr.bosszhipin:id/tv_search")
                tv_search.click()
                    #点击搜索
            print("此轮招呼已打完，程序结束，祝你找工作顺利！")
            #程序结束
        except Exception as e:
            print("代码运行错误，原因是：", str(e))
if __name__ == "__main__":
    unittest.main() #运行以上代码

