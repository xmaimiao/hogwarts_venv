'''
BasePage:存放一些基本的放大，比如：初始化 driver，find查找元素
'''
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        logging.info(f"find：{locator}")
        return self.driver.find_element(*locator)

    def find_eles(self, locator):
        logging.info(f"find_eles：{locator}")
        return self.driver.find_elements(*locator)

    def find_and_click(self, locator):
        logging.info("click")
        self.find(locator).click()

    def find_and_sendkeys(self, locator, text):
        logging.info(f"sendkeys：{text}")
        self.find(locator).send_keys(text)

    def find_scroll(self, text):
        logging.info("find_scroll")
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                                      '.scrollable(true).instance(0))'
                                                                      '.scrollIntoView(new UiSelector()'
        f'.text("{text}").instance(0));')

    def webdriver_wait(self, locator, timeout=20):
        logging.info(f"webdriver_wait：{locator},timeout：{timeout}")
        WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*locator))

    def back(self, num):
        logging.info(f"back：{num}")
        for i in range(num):
            self.driver.back()
