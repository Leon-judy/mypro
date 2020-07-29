'''
个人信息展示页，有更多按钮，设置备注和描述，邀请加入，发消息，语音通话
'''
from appium.webdriver.common.mobileby import MobileBy

from app_po.page.basepage import BasePage
from app_po.page.contactdetailsetting import ContactDetailSettingPage


class ContactDetailPage(BasePage):
    more_ele = (MobileBy.ID, "com.tencent.wework:id/guk")

    def contact_detail(self):
        # 点击..
        self.find_click(self.more_ele)
        return ContactDetailSettingPage(self.driver)
