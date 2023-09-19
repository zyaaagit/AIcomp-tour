import os
import requests
import json
from jsonsearch import JsonSearch

class LBSmap(object):
    def __init__(self):
        self.ak = self.read_ak()

    def read_ak(self):
        """ 持久化key, 便于读取 """
        ak = 'EE169070997731313807BEA5CB496C14097A0797FEEF15CA426XIZHFBT5E4083'
        return ak

    def request_url_get(self, url):
        """ 请求url方法get方法 """
        r = requests.get(url=url)
        return r.text

    def parse_json(self, content_json):
        """  解析json函数 """
        r_dict = json.loads(content_json)
        jsondata = JsonSearch(object=r_dict, mode='j')
        r_list = jsondata.search_all_value(key='name')   
        return r_list
    
    def request_api(self, url):
        """ 请求高德api解析json """
        result = self.request_url_get(url)
        city = self.parse_json(result)
        return city

    def run(self, address):
        """ 运行函数 """
        index_url = f'https://api.luokuang.com/v2/search/text?ak={self.ak}&keyword={address}&adcode=茂名'
        index_result = self.request_api(index_url)
        print(index_result)
        return index_result

