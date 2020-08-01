from functools import wraps

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

max_err_num = 3
error_num = 0


# 自身传入参数的装饰器（可以采用三层函数定义装饰器），这里以一个类来构建MyWraps装饰器
class MyWraps(object):

    def __init__(cls):
        cls._max_err_num = max_err_num
        cls._error_num = error_num

    def __call__(cls, func):
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']"),
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close1']")

        ]

        @wraps(func)
        # 增加self参数
        def wrapped_function(self, *args, **kwargs):
            try:
                # 增加self参数，可以调用finds方法
                func(self, *args, **kwargs)
            except Exception as e:
                # 如果元素没有找到，就进行黑名单查找处理
                if cls._error_num > cls._max_err_num:
                    # 如果error次数大于指定max，清空error次数并报异常
                    cls._error_num = 0
                    raise e
                cls._error_num += 1
                for ele in _black_list:
                    # 对黑名单进行点击
                    eles = self.finds(ele)
                    if len(eles) > 0:
                        # 以下语句不执行，即不关弹窗，直接返回让它再去找元素，会触发又一次查找黑名单
                        eles[0].click()
                        # 返回时func也要增加self参数
                        return func(self, *args, **kwargs)
                raise ValueError("没有黑名单")
            # 返回时func也要增加self参数
            return func(self, *args, **kwargs)

        return wrapped_function


class BasePage(object):
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self._error_num = error_num

    @MyWraps()
    def find(self, by, locator=None):
        # try:
        # 如果元素找到就清空error 计数
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        # self.error_num = 0 这里重置的语法好像有问题？？
        return result

    def finds(self, by, locator=None):
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def set_implicitly_wait(self, second):
        self.driver.implicitly_wait(second)
