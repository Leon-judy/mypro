'''
BasePage :存放一些基本的方法，比如：初始化 driver， find
'''
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        logging.info(f'find: {locator}')
        return self.driver.find_element(*locator)

    def finds(self, locator):
        logging.info(f'find: {locator}')
        return self.driver.find_elements(*locator)

    def find_click(self, locator):
        self.find(locator).click()
        logging.info(f'click: {locator}')

    def find_sendkeys(self, locator, text):
        self.find(locator).send_keys(text)
        logging.info(f'send keys: {text}')

    def web_until_ele_visibility(self, locator):
        logging.info(f'web driver wait: {locator}')
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def web_until_ele_visibility_click(self, locator):
        self.web_until_ele_visibility(locator).click()
        logging.info(f'click: {locator}')

    def web_until_ele_visibility_send_text(self, locator, text):
        self.web_until_ele_visibility(locator).send_keys(text)
        logging.info(f'send keys: {text}')

    def find_by_scroll(self, text):
        logging.info(f'find by scroll: {text}')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));'
                                        )

    def web_wait_lambda(self, locator, timeout=10):
        logging.info(f'web driver wait: {locator}')
        element = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))
        return element

    def back(self, num=1):
        for i in range(num):
            self.driver.back()
