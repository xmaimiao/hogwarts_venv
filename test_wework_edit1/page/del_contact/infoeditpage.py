from appium.webdriver.common.mobileby import MobileBy

from test_wework_edit1.page.basepage import BasePage
from test_wework_edit1.page.del_contact.contacteditpage import ContactEditPage


class InfoEditPage(BasePage):
    edit_button = (MobileBy.ID, 'com.tencent.wework:id/b2c')

    def contactedit(self):
        '''
        打开个人信息设置页面
        :return:
        '''
        # 点击 编辑成员,打开编辑成员页面
        self.find_and_click(self.edit_button)
        return ContactEditPage(self.driver)
