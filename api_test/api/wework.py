# coding:utf-8
import yaml
from api_test.api.baseapi import BaseApi


class WeWork(BaseApi):
    def __init__(self):
        # 调用父类的__init__完成父类的初始化
        super().__init__()
        with open("../api/wework.yml", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def test_create(self, userid, mobile, name="柯南", department=None):
        """
        创建成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        if department is None:
            department = "1"
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}"
        # data = {
        #     "userid": userid,
        #     "name": name,
        #     "department": department,
        #     "mobile": mobile
        # }
        # r = requests.post(url=url, json=data)
        # print(r.json())
        self.params["userid"] = userid
        self.params["name"] = name
        self.params["mobile"] = mobile
        self.params["department"] = department
        return self.send(self.data["mem_create"])

    def test_get(self, userid):
        """
        读取成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        self.params["userid"] = userid
        return self.send(self.data["mem_get"])

    def test_update(self, userid, name):
        """
        更新成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        self.params["userid"] = userid
        self.params["name"] = name
        return self.send(self.data["mem_update"])

    def test_delete(self, userid):
        """
        删除成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        self.params["userid"] = userid
        return self.send(self.data["mem_delete"])
