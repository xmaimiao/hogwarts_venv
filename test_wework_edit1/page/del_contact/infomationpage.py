from appium.webdriver.common.mobileby import MobileBy

from test_wework_edit1.page.basepage import BasePage
from test_wework_edit1.page.del_contact.infoeditpage import InfoEditPage


class InformationPage(BasePage):
    index_element = (MobileBy.ID, 'com.tencent.wework:id/h9p')

    def person_setting(self):
        '''
        打开个人信息页面
        :return:
        '''
        # 点击右上角设置符号，打开个人信息设置页面
        self.webdriver_wait(self.index_element)
        self.find_and_click(self.index_element)

        return InfoEditPage(self.driver)
