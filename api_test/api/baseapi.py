#!/usr/bin/env python
# coding:utf-8
# author:Leon
# datetime:2020/8/16 18:55
import requests
import json
from api_test.api.util import Util


class BaseApi:
    params = {}

    # 把数据进行变量替换,再发送出去

    def __init__(self):
        self.s = requests.session()
        self.s.params = {"access_token": Util().get_token()}

    def send(self, data):
        # 转化为json串
        raw_data = json.dumps(data)
        # print("\n@@", self.params)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        # print("@@替换后的send.raw_data : ", raw_data)
        # 转化为字典
        data = json.loads(raw_data)
        # print("@@send.data : ", data)
        return self.s.request(**data).json()
