from selenium.webdriver.common.by import By

from app_xueqiu.commons.basepage import BasePage
from app_xueqiu.page.optional.search import Search


class Market(BasePage):
    ele = (By.XPATH, "//*[contains(@resource-id,'/action_search')]")

    def goto_search(self):
        self.find(self.ele).click()
        return Search(self.driver)
