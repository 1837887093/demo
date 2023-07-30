import json
import requests
import os
import time
import datetime
import re


t = time.time()

def find_newest_file(directory):
    files = os.listdir(directory)
    if not files:
        return None
    newest_file = max(files, key=lambda x: os.path.getctime(os.path.join(directory, x)))
    return os.path.join(directory, newest_file)

directory = 'C:\CDG\zixuangu_android\data'
newest_file = find_newest_file(directory)

url = "https://zqact.tenpay.com/cgi-bin/guess_home.fcgi"
print(newest_file)

# 读取文件内容，并将其解析为JSON对象
with open(newest_file, 'r') as file:
    data = json.load(file)
# 获取body
body = data[0]['res']['body']
# 使用正则表达式提取fskey的值
match = re.search('"fskey":"([^"]+)"', body)
if match:
    fskey = match.group(1)
    print(fskey)
else:
    print("未找到fskey")

# 构造猜涨跌接口的参数
params = {
  "channel": "1",
  "source": "2",
  "expose_flag": "2",
  "new_version": "3",
  "_": int(round(t * 1000)),
  "openid": "oA0GbjpZFA4huIFFQGHLDpVg51kQ",
  "fskey": fskey,
  "access_token": "",
  "_appName": "android",
  "_appver": "10.5.0",
  "_osVer": "12",
  "_devId": "000000005714a932ffffffffef05ac4affffa932",
  "_ui": "000000005714a932ffffffffef05ac4affffa932"
}
print(params)

session = requests.Session()
response = requests.get(url, params=params)
# 检查请求是否成功
if response.status_code == 200:
    # 处理登录成功后的逻辑
    print("请求成功")
    # 查看响应的内容
    print("响应的内容:")
    print(json.dumps(response.json(), indent=2, sort_keys=True))

else:
    # 处理登录失败后的逻辑
    print("请求失败")
    print("cookies:", response.cookies)
