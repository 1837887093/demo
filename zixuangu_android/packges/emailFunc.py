import smtplib
from email.mime.text import MIMEText
# 发送多种类型的邮件
from email.mime.multipart import MIMEMultipart
import datetime

msg_from = '1837887093@qq.com'  # 发送方邮箱
passwd = 'nqivqbzjdkuzcaab'

to = ['1837887093@qq.com']  # 接受方邮箱

# 设置邮件内容
# MIMEMultipart类可以放任何内容
msg = MIMEMultipart()
# conntent="这个是字符串"
# #把内容加进去
# msg.attach(MIMEText(conntent,'plain','utf-8'))

# 添加附件
att1 = MIMEText(open('result.xlsx', 'rb').read(), 'base64', 'utf-8')  # 打开附件
att1['Content-Type'] = 'application/octet-stream'  # 设置类型是流媒体格式
att1['Content-Disposition'] = 'attachment;filename=result.xlsx'  # 设置描述信息

att2 = MIMEText(open('1.jpg', 'rb').read(), 'base64', 'utf-8')
att2['Content-Type'] = 'application/octet-stream'  # 设置类型是流媒体格式
att2['Content-Disposition'] = 'attachment;filename=1.jpg'  # 设置描述信息

msg.attach(att1)  # 加入到邮件中
msg.attach(att2)

now_time = datetime.datetime.now()
year = now_time.year
month = now_time.month
day = now_time.day
mytime = str(year) + " 年 " + str(month) + " 月 " + str(day) + " 日 "
fayanren = "爱因斯坦"
zhuchiren = "牛顿"
# 构造HTML
content = '''
        <html>
        <body>
          <h1 align="center">这个是标题，xxxx通知</h1>
          <p><strong>您好：</strong></p>
          <blockquote><p><strong>以下内容是本次会议的纪要,请查收！</strong></p></blockquote>

          <blockquote><p><strong>发言人：{fayanren}</strong></p></blockquote>
          <blockquote><p><strong>主持人：{zhuchiren}</strong></p></blockquote>
          <p align="right">{mytime}</p>
        <body>
        <html>
        '''.format(fayanren=fayanren, zhuchiren=zhuchiren, mytime=mytime)

msg.attach(MIMEText(content, 'html', 'utf-8'))

# 设置邮件主题
msg['Subject'] = "这个是邮件主题"

# 发送方信息
msg['From'] = msg_from

# 开始发送

# 通过SSL方式发送，服务器地址和端口
s = smtplib.SMTP_SSL("smtp.qq.com", 465)
# 登录邮箱
s.login(msg_from, passwd)
# 开始发送
s.sendmail(msg_from, to, msg.as_string())
print("邮件发送成功")