from time import sleep

from selenium.webdriver.common.by import By

from app_xueqiu.commons.basepage import BasePage
from app_xueqiu.page.optional.market import Market


class Main(BasePage):
    ele = (By.XPATH, "//*[contains(@resource-id,'android:id/tabhost')]//*[@text='行情']")
    ele1 = (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")

    def goto_market(self):
        # 伪造黑名单，点击登录
        self.find(self.ele1).click()
        sleep(2)
        self.find(self.ele).click()
        self.set_implicitly_wait(5)
        return Market(self.driver)
