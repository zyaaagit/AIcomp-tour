import os
import requests
import xml.etree.ElementTree as ET

class GDmap(object):
    def __init__(self):
        self.key = self.read_key()

    def read_key(self):
        """ 持久化key, 便于读取 """
        key = '4eebece011fa2f37fb741be854065655'
        return key

    def request_url_get(self, url):
        """ 请求url方法get方法 """
        r = requests.get(url=url)
        return r.text

    def parse_json(self, content_json):
        """  解析json函数 """
        root = ET.fromstring(content_json)
        if root.find('.//count').text != '0':
            content = root.find('.//city').text
            return content
        return None
    
    def request_api(self, url):
        """ 请求高德api解析json """
        result = self.request_url_get(url)
        city = self.parse_json(result)
        return city

    def run(self, address):
        """ 运行函数 """
        index_url = f'https://restapi.amap.com/v3/geocode/geo?address={address}&output=XML&key={self.key}'
        index_result = self.request_api(index_url)
        return index_result

