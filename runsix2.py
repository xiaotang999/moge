# 采集六合程序 run6h.py
import requests
import json
import datetime
import time
#
n_time = datetime.datetime.now().strftime('%H%M')#现在
print(n_time)

    # {
    # "id":"122",
    # "time":"21:43:0",
    # "nextid":"123",
    # "s":0,
    # "c":"4001",
    # "ma":"45,虎,red,1,狗,red,15,猴,blue,5,马,green,39,猴,green,47,鼠,blue,43,龙,green",
    # "year":"2018",
    # "m":"",
    # "day":"10月27日",
    # "type":4,
    # "nextdate":"2018/10/30 21:30:00",
    # "info":""
    # }

def six2():
    _url = "http://1680660.com/smallSix/findCurrentVideoInfo.do"
    _get_token = "kdsjfhsh29*/djk.*3dsa.1x1as"
    _get_url = "http://127.0.0.9/opengotwo/"
    r = requests.get(_url)
    _json = r.json()

    _id = _json['id']
    _time = _json['time']
    _nextid = _json['nextid']
    _ma = _json['ma']
    _type = _json['type']
    _nextdate = _json['nextdate']

    data = {
            "token": _get_token,
            "id": _id,
            "time": _time,
            "nextid": _nextid,
            "ma": _ma,
            "type": _type,
            "nextdate": _nextdate,
        }
    print(data)
    xx = requests.get(_get_url, data)
    print(xx)        






def xunhuan():
    #six()
    #print("循环开始")
    s_time = 2130 #开始时间
    e_time = 2140 #结束时间
    now_time = datetime.datetime.now().strftime('%H%M')#现在
    #print(now_time)
    now_time = int(now_time)
    #zhi = now_time - s_time
    if now_time > s_time:
        #print("start")
        if now_time < e_time:
            print("开始执行")
            try:
                six2()
            except:
                pass
                
# while True:
#     xunhuan()
#     time.sleep(4)
try:
    six2()
except:
    print("bug")