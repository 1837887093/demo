import unittest
from packges.HTMLTestRunner import HTMLTestRunner
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import os.path

suite = unittest.TestSuite()
#实例化TestSuite到套件suite里

case = unittest.defaultTestLoader.discover(start_dir="case",pattern="zxg_general.py")
#使用discover方法，批量导入测试用例，start.dir是路径，pattern是文件名，最后再定义到变量case里面

suite.addTest(case)
#添加case到套件里

now = time.strftime("%Y.%m.%d_%H.%M.%S")  # 修改日期时间格式，使用斜杠和冒号作为分隔符
path = r'C:\\CDG\\zixuangu_android\\report\\自选股安卓测试报告-{}.html'.format(now)
with open(path,"wb") as f:
    runner = HTMLTestRunner(stream=f,title='每日报告',description='腾讯自选股安卓端测试报告')
#实例化runner方法，使用HTMLTestRunner方法（从网上下载PY文件，放到指定目录，再导入这个包，可指定报告名称，详细描述）
    runner.run(suite)
#使用runner运行suite

# 设置相关参数
report_path = path
sender_email = '1837887093@qq.com'  # 发件人邮箱
sender_password = 'nqivqbzjdkuzcaab'  # 发件人邮箱密码或授权码
receiver_email = '1837887093@qq.com'  # 接收人邮箱
subject = '自选股安卓测试报告'  # 邮件主题

def send_email(report_path, sender_email, sender_password, receiver_email, subject):
    # SMTP服务器设置（根据您的邮箱提供商进行相应设置）
    smtp_server = 'smtp.qq.com'
    smtp_port = 465

    # 构造邮件
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 添加邮件正文
    body = MIMEText('这是一封测试报告，请查收。')
    msg.attach(body)

    # 添加测试报告附件
    with open(report_path, 'rb') as file:
        attachment = MIMEApplication(file.read())
    attachment.add_header('Content-Disposition', 'attachment', filename='测试报告.html')
    msg.attach(attachment)

    # 发送邮件
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("邮件发送失败：", str(e))

# 调用函数发送邮件
send_email(report_path, sender_email, sender_password, receiver_email, subject)