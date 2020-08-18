#!/usr/bin/env python
# coding:utf-8
# author:Judy
# datetime:2020/8/17 21:50
import yaml

from api_test.api.baseapi import BaseApi


class Tag(BaseApi):
    def __init__(self):
        super().__init__()
        with open("../api/wework.yml", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def tag_create(self, tagname, tagid):
        """
        创建标签
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        :param tagname:
        :param tagid:
        :return:
        """
        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        return self.send(self.data["tag_create"])

    def tag_update(self, tagid, tagname):
        """
        更新标签
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
        :return:
        """
        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        return self.send(self.data["tag_update"])

    def tag_get(self, tagid):
        """
        获取tag
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=TAGID
        :param tagid:
        :return:
        """
        self.params["tagid"] = tagid
        return self.send(self.data["tag_get"])

    def tag_delete(self, tagid):
        """
        删除标签
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        :param tagid:
        :return:
        """
        self.params["tagid"] = tagid
        return self.send(self.data["tag_delete"])
