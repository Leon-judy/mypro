'''
通讯录列表页面
'''
from appium.webdriver.common.mobileby import MobileBy

from app_po.page.addmemberpage import AddMemberPage
from app_po.page.basepage import BasePage
from app_po.page.departmentsearchpage import DepartmentSearchPage


class ContactListPage(BasePage):
    web_view1 = "添加成员"
    search_ele = (MobileBy.ID, "com.tencent.wework:id/guu")

    def add_contact(self):
        # 3. 点击添加成员

        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          f'.text("{webview1}").instance(0));'
        #                          ).click()
        self.find_by_scroll(self.web_view1).click()
        return AddMemberPage(self.driver)

    def search_contact(self):
        # 1. 点击搜索框
        self.find_click(self.search_ele)
        return DepartmentSearchPage(self.driver)
