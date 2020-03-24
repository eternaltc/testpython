# #coding:utf-8

import json
import requests
# import csv
from urllib.request import Request, urlopen
#这里就是组装请求参数（航班号要通过接口获取）
values = {"flightId":"EB16C5D2CAD54088933770317A3F1ABE"}
 # 打印values的数据类型,输出<class 'dict'>
values_json = json.dumps(values)
#zb网站获取数据Api
url = "https://api-iaoc-t.redair.cn/rest/dcs/lfsd?token=1&channel=redair"
values_json = json.dumps(values)
print("组装的json",values_json)
 # requests库提交数据进行post请求
 #这一步就是请求接口
req = requests.post(url, data=values_json)
 # 打印Unicode编码格式的json数据
print("获取到的返回消息",req.text)
#解析json 数据，生成csv文件
# 转换成json格式
jsonsObject  = json.loads(req.text)
print("转换的json数据",jsonsObject)
jsonsresult = jsonsObject["result"]
print("解析后获取的json数据",jsonsresult)
#把获取的数据生成csv文件




#包装头部

