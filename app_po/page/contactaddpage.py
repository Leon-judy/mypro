'''
手动输入成员信息页面
'''
# from app_po.page.addmemberpage import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app_po.page.basepage import BasePage


class ContactAddPage(BasePage):
    name_ele = (MobileBy.XPATH,
                '//*[contains(@text,"姓名")]/../*[@class="android.widget.EditText"]')
    set_gender_ele = (MobileBy.XPATH,
                      '//*[contains(@text,"性别")]/..//*[@text="男"]')
    male_ele = (MobileBy.XPATH, '//*[@text="男"]')
    famale_ele = (MobileBy.XPATH, '//*[@text="女"]')
    phone_num = (MobileBy.XPATH, '//*[contains(@text,"手机号")]')
    save_ele = (MobileBy.XPATH, '//*[@text="添加成员"]/ancestor::*//*[@text="保存"]')

    def set_name(self, name):
        # self.driver.find_element(MobileBy.XPATH,
        #                          '//*[contains(@text,"姓名")]/../*[@class="android.widget.EditText"]').send_keys(name)
        self.find_sendkeys(self.name_ele, name)
        return self

    def set_gender(self, gender):
        # self.driver.find_element(MobileBy.XPATH,
        #                          '//*[contains(@text,"性别")]/..//*[@text="男"]').click()
        self.find_click(self.set_gender_ele)
        if gender == "男":
            # WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((MobileBy.XPATH, '//*[@text="男"]'))
            # ).click()
            self.web_until_ele_visibility_click(self.male_ele)

        else:
            # WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((MobileBy.XPATH, '//*[@text="女"]'))
            # ).click()
            self.web_until_ele_visibility_click(self.famale_ele)
        return self

    def set_phone_num(self, phone_num):
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机号")]').send_keys(phone_num)
        self.find_sendkeys(self.phone_num, phone_num)
        return self

    def click_save(self):
        from app_po.page.addmemberpage import AddMemberPage
        # 6.点击保存
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]/ancestor::*//*[@text="保存"]').click()
        self.find_click(self.save_ele)
        return AddMemberPage(self.driver)
