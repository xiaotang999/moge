# 采集六合程序 run6h.py
import requests
import json
import datetime
import time
#
n_time = datetime.datetime.now().strftime('%H%M')#现在
print(n_time)
def six():
    _token = "781abd11a87b6115"
    _url = "http://api.b1cp.com/api?p=json&t=hk6&limit=1&token="+_token
    _get_token = "kdsjfhsh29*/djk.*3dsa.1x1as"
    _get_url = "http://127.0.0.9/getsixone/"
    r = requests.get(_url)
    _json = r.json()
    print(_json)


    
    # _expect = _json['data'][0]['expect']
    # _opencode = _json['data'][0]['opencode']
    # _opentime = _json['data'][0]['opentime']
    # _Str = _opencode.split(',')
    # _no_1 = _Str[0]
    # _no_2 = _Str[1]
    # _no_3 = _Str[2]
    # _no_4 = _Str[3]
    # _no_5 = _Str[4]
    # _no_6 = _Str[5]
    # _no_7 = _Str[6]
    # data = {
    #         "token": _get_token,
    #         "expect": _expect,
    #         "no1": _no_1,
    #         "no2": _no_2,
    #         "no3": _no_3,
    #         "no4": _no_4,
    #         "no5": _no_5,
    #         "no6": _no_6,
    #         "no7": _no_7,
    #     }
    # print(data)
    # xx = requests.get(_get_url, data)
    # print(xx)
#
# def xunhuan():
#     #six()
#     #print("循环开始")
#     s_time = 2130 #开始时间
#     e_time = 2140 #结束时间
#     now_time = datetime.datetime.now().strftime('%H%M')#现在
#     #print(now_time)
#     now_time = int(now_time)
#     #zhi = now_time - s_time
#     if now_time > s_time:
#         #print("start")
#         if now_time < e_time:
#             print("开始执行")
#             try:
#                 six()
#             except:
#                 pass
                
# while True:
#     xunhuan()
#     time.sleep(4)
