import os
import requests
import json
import xml.etree.ElementTree as ET

class BDmap(object):
    def __init__(self):
        self.ak = self.read_ak()

    def read_ak(self):
        """ 持久化key, 便于读取 """
        ak = 'qGB7PbSyD7PTb6eG9v6v0BRCX62Ng6Mg'
        return ak

    def request_url_get(self, url):
        """ 请求url方法get方法 """
        r = requests.get(url=url)
        return r.text

    def parse_json(self, content_json):
        """  解析json函数 """
        r_dict = json.loads(content_json)
        len_dict = len(r_dict['results'])
        r_list = set()
        if len_dict == 0:
            return None
        else:
            for i in range(len_dict):
                r_list.add(r_dict['results'][i]['name'])
        return r_list
    
    def request_api(self, url):
        """ 请求高德api解析json """
        result = self.request_url_get(url)
        city = self.parse_json(result)
        return city

    def run(self, address):
        """ 运行函数 """
        index_url = f'https://api.map.baidu.com/place/v2/search?query={address}&region=茂名&city_limit=true&output=json&ak={self.ak}'
        index_result = self.request_api(index_url)
        return index_result

