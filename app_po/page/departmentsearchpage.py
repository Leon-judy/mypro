'''
搜索页面
'''
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_po.page.basepage import BasePage


# from app_po.page.contactdetailpage import ContactDetailPage


# noinspection PyGlobalUndefined
class DepartmentSearchPage(BasePage):
    name_text_input = (MobileBy.ID, "com.tencent.wework:id/fk1")

    def __init__(self, driver):
        self.driver = driver
        self.ele_list = None
        self.ele_list_after = None
        self.name_list_get = None

    def department_search(self, name):
        # 按模糊查询“name”的姓名
        self.name_list_get = (MobileBy.XPATH, f'//*[contains(@text,"{name}")]')
        # 2. 输入联系人姓名
        self.find_sendkeys(self.name_text_input, name)

        sleep(3)

        # 3. 获取联系人列表

        self.ele_list = self.finds(self.name_list_get)
        return self.ele_list

    def goto_contact_detail_page(self, ele_list):
        # 4. 判断搜索出来的列表长度
        if len(ele_list) < 2:
            print("没有搜索出来")
            return
        # 存在联系人，点击第一个
        else:
            ele_list[1].click()

        from app_po.page.contactdetailpage import ContactDetailPage
        return ContactDetailPage(self.driver)
