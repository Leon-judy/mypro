'''
编辑成员页面，修改姓名/账号/别名/性别/座机/邮箱...删除成员
'''
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_po.page.basepage import BasePage


# from app_po.page.departmentsearchpage import DepartmentSearchPage


class ContactEditPage(BasePage):
    text = "删除成员"
    determine_ele = (MobileBy.XPATH, '//*[@text="确定"]')

    def contact_edit(self):
        self.find_by_scroll(self.text).click()

        self.web_until_ele_visibility_click(self.determine_ele)
        sleep(2)

        from app_po.page.departmentsearchpage import DepartmentSearchPage
        return DepartmentSearchPage(self.driver)
