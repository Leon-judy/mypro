#!/usr/bin/env python
# coding:utf-8
# author:Leon
# datetime:2020/8/16 18:54
import re
import pytest
from hamcrest import *
from api_test.api.wework import WeWork


class TestWeWork:
    @pytest.mark.parametrize("userid, mobile", [("kenan" + str(x), "134%08d" % x) for x in range(1, 2)])
    def test_create(self, userid, mobile):
        r = WeWork().test_create(userid, mobile)
        print(r)
        return r

    @pytest.mark.parametrize("userid", ["kenan" + str(x) for x in range(8, 9)])
    def test_get(self, userid):
        r = WeWork().test_get(userid)
        return r

    @pytest.mark.parametrize("userid, name", [("kenan" + str(x), "really" + str(x),) for x in range(2, 5)])
    def test_update(self, userid, name):
        r = WeWork().test_update(userid, name)
        return r

    @pytest.mark.parametrize("userid", ["kenan" + str(x) for x in range(1, 2)])
    def test_delete(self, userid):
        r = WeWork().test_delete(userid)
        return r

    @pytest.mark.parametrize("userid, name, mobile",
                             [("kenan" + str(x), "kenan" + str(x), "134%08d" % x) for x in range(2)])
    def test_wework(self, userid, name, mobile):
        """
        整体测试
        :return:
        """
        try:
            # print(userid, mobile)
            assert "created" == self.test_create(userid, mobile)["errmsg"]
        except AssertionError as e:
            print("error: ", e)
            if "mobile existed" in e.__str__():
                re_userid = re.findall(":(.*)'$", e.__str__())[0]
                assert "deleted" == self.test_delete(re_userid)["errmsg"]
                assert "created" == self.test_create(userid, mobile)["errmsg"]
        assert "updated" == self.test_update(userid, name="new user")["errmsg"]
        assert "new user" == self.test_get(userid)["name"]
        assert "deleted" == self.test_delete(userid)["errmsg"]
        assert_that(self.test_get(userid)["errmsg"], contains_string("not found"))
