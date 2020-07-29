# from test_wework_edit1.page.searchpage import SearchPage
from appium.webdriver.common.mobileby import MobileBy

from test_wework_edit1.page.basepage import BasePage


class ContactEditPage(BasePage):
    del_button = (MobileBy.ID, 'com.tencent.wework:id/e3f')
    confirm_element = (MobileBy.ID, 'com.tencent.wework:id/bci')

    def contactdelpage(self):
        '''
        打开编辑成员页面
        :return:
        '''
        # 点击 删除成员，返回到搜索页面
        self.find_and_click(self.del_button)
        self.find_and_click(self.confirm_element)
        from test_wework_edit1.page.del_contact.searchpage import SearchPage
        return SearchPage(self.driver)
