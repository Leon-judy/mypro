'''
添加成员页面
'''
# 会与后面contactaddpage.py中的导入形成循环导入：circular immport
# from app_po.page.contactaddpage import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app_po.page.basepage import BasePage


class AddMemberPage(BasePage):
    add_manual_ele = (MobileBy.XPATH,
                      '//android.widget.TextView[@text="手动输入添加"]')
    get_toast_ele = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def add_manual(self):
        '''
        手动输入添加
        :return:
        '''
        # 局部导入
        from app_po.page.contactaddpage import ContactAddPage
        # 4. 手动输入添加
        # self.driver.find_element(MobileBy.XPATH,
        #                          '//android.widget.TextView[@text="手动输入添加"]').click()
        self.find_click(self.add_manual_ele)
        return ContactAddPage(self.driver)

    def get_toast(self):
        # 7.验证添加成功
        # self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        # element = WebDriverWait(self.driver, 10).until(
        #     lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))

        result = self.web_wait_lambda(self.get_toast_ele).text
        return result
