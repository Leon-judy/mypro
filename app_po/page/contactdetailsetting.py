'''
个人信息设置页，有设置备注和描述，推荐给联系人，设为星标联系人，添加到手机通讯录，编辑成员
'''
from appium.webdriver.common.mobileby import MobileBy

from app_po.page.basepage import BasePage
from app_po.page.contacteditpage import ContactEditPage


class ContactDetailSettingPage(BasePage):
    edit_ele = (MobileBy.XPATH, '//*[@text="编辑成员"]')

    def contact_detail_setting(self):
        # 点击编辑成员
        self.find_click(self.edit_ele)

        return ContactEditPage(self.driver)
