import json
import requests

url = "https://wzq.tenpay.com/cgi-bin/welfare_center.fcgi"

# 构造登录接口的参数
params = {
  "action": "home",
  "channel": "1",
  "sign_actid": "2002",
  "daily_task_actid": "1111",
  "continue_task_actid": "1030",
  "zxgmp_lct": "0",
  "suprise_position": "welfare",
  "_": "1689671191708",
  "openid": "oA0GbjpZFA4huIFFQGHLDpVg51kQ",
  "fskey": "v0ba829662064b653a74f0f46d44f76c",
  "access_token": "",
  "_appName": "android",
  "_appver": "10.5.0",
  "_osVer": "12",
  "_devId": "000000005714a932ffffffffef05ac4affffa932",
  "_ui": "000000005714a932ffffffffef05ac4affffa932"
}

response = requests.get(url, params=params)

# 检查请求是否成功
if response.status_code == 200:
    # 处理登录成功后的逻辑
    print("请求成功")
    # 查看响应的内容
    print("响应的内容:")
    print(json.dumps(response.json(), indent=2, sort_keys=True))
    print("cookies:", response.cookies)
else:
    # 处理登录失败后的逻辑
    print("请求失败")
    print("cookies:", response.cookies)

'''
#发送一个get请求并得到响应
r = requests.get('https://zqact.tenpay.com/cgi-bin/guess_home.fcgi')
#查看响应对象的类型
print(type(r))
#查看响应状态码
print(r.status_code)
#查看响应内容的类型
print("内容的类型:",type(r.text))
#查看响应的内容
print("响应的内容:",r.text)
#查看cookies
print("cookies:",r.cookies)
'''
