'''
主页面
'''
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app_po.page.basepage import BasePage
from app_po.page.contactlistpage import ContactListPage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    contact_list = (MobileBy.XPATH, '//android.widget.TextView[@text="通讯录"]')

    def goto_contact_list(self):
        '''
        进入到通讯录页面
        :return:
        '''
        # 2. 点击通讯录
        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(
        #         (MobileBy.XPATH, '//android.widget.TextView[@text="通讯录"]'))).click()
        self.web_until_ele_visibility_click(self.contact_list)
        return ContactListPage(self.driver)

    def goto_work_bench(self):
        '''
        进入到工作台页面
        :return:
        '''
        pass

    def goto_me(self):
        '''
        进入到通讯录页面
        :return:
        '''
        pass
