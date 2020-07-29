'''
存放app应用常用的一些方法：比如启动app，关闭app，停止app，进入首页
'''
from appium import webdriver

from app_po.page.basepage import BasePage
from app_po.page.mainpage import MainPage


class App(BasePage):

    def start(self):
        '''
        启动app
        :return:
        '''
        if self.driver == None:
            # 第一次调用start()方法时，driver为None
            desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                # "automationName": "UiAutomator2",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": True,  # True表示不要在会话前重置应用状态。默认值false,每次登录会初始化清空缓存/一些登录的信息
                "skipServerInstallation": True,  # 跳过uiaoutomator2 server的安装
                # "dontStopAppOnReset": True,  # 启动之前不停止app
                "skipDeviceInitialization": True,  # 跳过设备初始化
                "adbExecTimeout": 50000,
                'settings[waitForIdleTimeout]': 0  # 等待空闲的状态
            }

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            # 这个方法不需要传入任何参数，会自动启动起来desired_caps里面定义的activity
            self.driver.launch_app()
            # 可以启动其它的应用的页面
            # self.driver.start_activity(app_package=None, app_activity=None)
        self.driver.implicitly_wait(20)
        # 外面调用start方法后仍返回到App()类,
        # 可以继续调用App()类的其他方法
        return self

    def restart(self):
        '''
        重启app
        :return:
        '''
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        '''
        停止app
        :return:
        '''
        self.driver.quit()

    def goto_main(self):
        '''
        进入首页
        :return:
        '''
        return MainPage(self.driver)
