from appium.webdriver.common.mobileby import MobileBy
from test_wework_edit1.page.basepage import BasePage
from test_wework_edit1.page.add_contact.contactlistpage import ContactListPage


class MainPage(BasePage):
    index_ele = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def goto_contactlist(self):
        '''
        进入到通讯录
        :return:
        '''
        self.webdriver_wait(self.index_ele)
        self.find_and_click(self.index_ele)
        return ContactListPage(self.driver)

    def goto_workbench(self):
        pass
