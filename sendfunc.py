# coding=utf-8

import requests
import json
import time

class RunMain:

    def send_post(self, url, data):
        result = requests.post(url=url, data= data)
        print(result)
        #res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def send_get(self, url, data):
        result = requests.get(url=url, data= data)
        print(result)      
        if isinstance(result, str):       # 首先判断变量是否为字符串
            try:
                res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
                return res
            except ValueError:
                pass
                return result
        else:
            return result

    def run(self,method, url=None, data=None):
        if method.upper() =='POST':
            self.send_post(url,data)
        elif method.upper() == 'GET':
            self.send_get(url,data)
        else:
            pass

if __name__ =='__main__':
    rm = RunMain()
    timestamp = round(time.time()*1000)
    rm.run('post','https://dtc-api-test.zcloud.ac.cn/api/gov/publickey',timestamp)
    

    