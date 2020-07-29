from appium import webdriver
from test_wework_edit1.page.basepage import BasePage
from test_wework_edit1.page.mainpage import MainPage


class App(BasePage):
    _package = 'com.tencent.wework'
    _activity = '.launch.LaunchSplashActivity'

    def start(self):
        '''
        启动APP
        :return:
        '''
        if self.driver == None:
            caps = dict()
            caps["platformName"] = 'Android'
            caps["deviceName"] = '127.0.0.1:7555'
            caps["platformVersion"] = '6.0.1'
            caps["appPackage"] = self._package
            caps["automationName"] = 'uiautomator2'
            caps["appActivity"] = self._activity
            caps["noReset"] = 'true'
            # 启动之前不关闭APP
            # caps["dontStopAppOnReset"] = 'true'
            caps["skipDeviceInitializati"] = 'true'
            caps["chromedriverExecutable"] = 'C:\Program Files (x86)\Appium\chromedriver2.20.exe'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self.driver.start_activity(self._package, self._activity)
        self.driver.implicitly_wait(30)
        return self

    def stop(self):
        '''
        停止APP
        :return:
        '''
        self.driver.quit()

    def restart(self):
        '''
        重启APP
        :return:
        '''
        self.driver.close()
        # 启动应用
        self.driver.launch_app()
        return self

    def goto_main(self):
        '''
        进入首页
        :return:
        '''
        return MainPage(self.driver)
