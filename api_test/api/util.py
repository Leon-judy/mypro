#!/usr/bin/env python
# coding:utf-8
# author:Leon
# datetime:2020/8/16 18:56
import requests


class Util:
    def get_token(self):
        """
        获取token
        请求方式： GET（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        data = {
            "corpid": "ww76495251b65eb217",
            "corpsecret": "A1iLXzwcJV_pl4ZAxPq7tYTGV9U5w9MZ7UXtAVFOktk"
        }
        # 第一种Get传参：使用？携带参数
        #  r = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww76495251b65eb217&
        #  corpsecret=A1iLXzwcJV_pl4ZAxPq7tYTGV9U5w9MZ7UXtAVFOktk")
        # 第二种get传参：将携带的参数传给params
        r = requests.get(
            url=url, params=data)
        # print(r.json())
        return r.json()['access_token']
