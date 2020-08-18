#!/usr/bin/env python
# coding:utf-8
# author:Judy
# datetime:2020/8/17 19:36
import random
import re
import pytest
from hamcrest import *

from api_test.api.tag import Tag
from api_test.api.wework import WeWork


class TestTag:
    @pytest.mark.parametrize("tagname, tagid", [("tag" + str(random.randint(0, 99999)), str(x)) for x in range(20, 22)])
    def test_tag_create(self, tagname, tagid):
        r = Tag().tag_create(tagname, tagid)
        print(r)
        return r

    @pytest.mark.parametrize("tagid", [str(x) for x in range(1, 6)])
    def test_tag_get(self, tagid):
        r = Tag().tag_get(tagid)
        print(r)
        return r

    @pytest.mark.parametrize("tagid, tagname",
                             [(str(x), "re_tag" + str(random.randint(0, 99999)),) for x in range(1, 6)])
    def test_tag_update(self, tagid, tagname):
        r = Tag().tag_update(tagid, tagname)
        print(r)
        return r

    @pytest.mark.parametrize("tagid", [str(x) for x in range(1, 30)])
    def test_tag_delete(self, tagid):
        r = Tag().tag_delete(tagid)
        print(r)
        return r

    @pytest.mark.parametrize("tagid, tagname",
                             [(str(x), "tag" + str(random.randint(0, 99999))) for x in range(1, 6)])
    def test_tag(self, tagid, tagname):
        """
        整体测试
        :return:
        """
        try:
            assert "created" == self.test_tag_create(tagname, tagid)["errmsg"]
        except AssertionError as e:
            print("error:", e)
            if "invalid tagid" in e.__str__():
                assert "deleted" == self.test_tag_delete(tagid)["errmsg"]
                assert "created" == self.test_tag_create(tagname, tagid)["errmsg"]
        new_name = "re_tag" + str(random.randint(0, 99999))
        assert "updated" == self.test_tag_update(tagid, new_name)["errmsg"]
        assert new_name == self.test_tag_get(tagid)["tagname"]
        assert "deleted" == self.test_tag_delete(tagid)["errmsg"]
        assert_that(self.test_tag_get(tagid)["errmsg"], contains_string("invalid tagid"))
