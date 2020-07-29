import pytest
import yaml

from app_po.page.app import App
from app_po.page.basepage import BasePage

with open("../data/mydata1.yml") as f:
    datas_add = yaml.safe_load(f)
with open("../data/mydata_del.yml") as f:
    datas_del = yaml.safe_load(f)


class TestContact:

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize("name, gender, phone_num", datas_add)
    def test_add_contact(self, name, gender, phone_num):
        '''
        添加联系人
        :param name: name032, name033, name034
        :param gender: 男, 男, 女
        :param phone_num: 13471011032， 13471011033， 13471011034
        :return:
        '''
        # name = "name013"
        # gender = "男"
        # phone_num = "13471234013"
        my_page = self.main.goto_contact_list(). \
            add_contact().add_manual(). \
            set_name(name).set_gender(gender). \
            set_phone_num(phone_num).click_save()
        text = my_page.get_toast()
        assert '成功' in text
        self.app.back()

    @pytest.mark.parametrize("name", datas_del)
    def test_del_contact(self, name):
        '''
        删除联系人
        :param name: 删除包含了name的姓名的人：name03, name03, name03
        :return:
        '''
        # 进入搜索框之后的页面保存到my_page
        my_page = self.main.goto_contact_list().search_contact()
        # 删除前，把查询的姓名列表保存
        ele_list = my_page.department_search(name)
        # 从查询到的姓名列表中选择一个click继续向后执行
        my_page2 = my_page.goto_contact_detail_page(ele_list). \
            contact_detail().contact_detail_setting().contact_edit()
        # 删除后，把查询的姓名列表保存
        ele_list_after = my_page.department_search(name)
        assert len(ele_list) - len(ele_list_after) == 1
        self.app.back()
