from selenium.webdriver.common.by import By

from app_xueqiu.commons.basepage import BasePage


class Search(BasePage):
    ele = (By.XPATH, "//*[@class='android.widget.EditText']")

    def search(self, name_find):
        self.ele_result = (By.XPATH, f"//*[@text='{name_find}' and @resource-id='com.xueqiu.android:id/name']")
        self.ele_add_optional = (By.XPATH,
                                 f"//*[contains(@resource-id,'stock_result_view')]//*[@text='{name_find}']/../..//*[@text='加自选']")

        # 输入要查询的名字
        self.find(self.ele).send_keys(name_find)
        self.driver.keyevent(66)
        # 在查询结果列表中找到需要的那个点击
        self.find(self.ele_result).click()
        # 在综合列表中把“阿里巴巴-SW”加自选
        self.find(self.ele_add_optional).click()

    def is_choose(self, name_find):
        self.ele_add = (By.XPATH,
                        f"//*[contains(@resource-id,'stock_result_view')]//*[@text='{name_find}']/../..//*[@text='已添加']")
        eles = self.finds(self.ele_add)
        return len(eles) > 0
