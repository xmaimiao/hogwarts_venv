import time
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAW:
    def setup(self):
        caps = {}
        caps["platformName"] = 'Android'
        caps["deviceName"] = '192.168.111.101:5555'
        caps["platformVersion"] = '6.0'
        caps["appPackage"] = 'com.xueqiu.android'
        caps["automationName"] = 'uiautomator2'
        caps["appActivity"] = '.common.MainActivity'
        caps["noReset"] = 'true'
        caps["dontStopAppOnReset"] = 'true'
        caps["skipDeviceInitializati"] = 'true'
        caps["unicodeKeyboard"] = 'true'
        caps["resetKeyboard"] = 'true'
        caps["chromedriverExecutable"] = 'C:\Program Files (x86)\Appium\chromedriver74.exe'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        self.driver.back()

    def test_xueqiu_aw(self):
        """
        1.打開雪球 APP
        2.點擊“交易”
        3.點擊“A股開戶”
        4.在輸入用戶名和密碼
        5.點擊“立即開戶”
        6.退出應用
        :return:
        """

        # 2.點擊“交易”
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()
        A_locator = (MobileBy.XPATH, '//*[@class="trade_home_agu_3ki"]/div[2]/h1')

        # 获取当前上下文
        print(self.driver.contexts)
        # 在这里获取当前窗口句柄就会报错
        # print(self.driver.window_handles)
        self.driver.switch_to.context(self.driver.contexts[1])
        # 切換到H5頁面後再打印當前窗口句柄不會出錯
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(A_locator))

        # 3.點擊“A股開戶”
        self.driver.find_element(*A_locator).click()
        print(self.driver.window_handles)

        # 获取当前打开的窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phonenumber_locator = (MobileBy.ID, 'phone-number')
        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable(phonenumber_locator))

        # 4.在輸入用戶名和密碼，點擊“立即開戶”
        self.driver.find_element(*phonenumber_locator).send_keys('18218813163')
        self.driver.find_element(MobileBy.ID, 'code').send_keys('123456')
        self.driver.find_element(MobileBy.XPATH, '/html/body/div/div/div[2]/div/div[2]/h1').click()

        # 获取toast文本
        while True:
            # toast_text = self.driver.find_element(By.XPATH,'//*[text()="请先获取验证码"]').is_displayed()  true
            # toast_text = self.driver.find_element(MobileBy.XPATH, '//*[text()="请先获取验证码"]').is_displayed()  true
            toast_text = self.driver.find_element(MobileBy.XPATH, '//*[@class="toast"]').is_displayed()
            if toast_text:
                break

        self.driver.back()
        assert toast_text == True
