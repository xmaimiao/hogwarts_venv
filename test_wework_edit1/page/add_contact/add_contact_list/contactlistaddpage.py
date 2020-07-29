from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_wework_edit1.page.basepage import BasePage


class ContactListAddPage(BasePage):
    def weworkadd(self, name):
        # 滾動查找人员，點擊  添加
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #                                                        'scrollable(true).instance(0)).'
        #                                                        'scrollIntoView(new UiSelector().'
        #                                                       f'text("{name}").instance(0));')
        self.find_scroll(name)
        member_ele = (MobileBy.XPATH, f"//*[@text='{name}']/../../../..//*[@text='添加']")
        # WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(member_ele))
        # self.driver.find_element(*member_ele).click()
        self.webdriver_wait(member_ele)
        self.find_and_click(member_ele)
        sleep(3)
        addlist_ele = (MobileBy.XPATH, f"//*[@text='{name}']/../../../*[@text='加入企业通讯录']")
        # self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']/../../../*[@text='加入企业通讯录']").click()
        self.find_and_click(addlist_ele)
        added_ele = (MobileBy.XPATH, f"//*[@text='{name}']/../../../*[@text='已加入']")
        # result = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']/../../../*[@text='已加入']").click()
        result = self.find(added_ele).text
        return result
