from appium.webdriver.common.mobileby import MobileBy

from test_wework_edit1.page.add_contact.add_contact_list.contactlistaddpage import ContactListAddPage
from test_wework_edit1.page.basepage import BasePage


class AddMemberPage(BasePage):
    manual_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    text_ele = (MobileBy.XPATH, "//*[contains(@text,'添加成功')]")
    list_element = (MobileBy.XPATH, '//*[@text="从微信/手机通讯录中添加"]')

    def add_menual(self):
        '''
        手动输入添加
        :return:
        '''
        # 点击 “手动添加人员”
        self.find_and_click(self.manual_element)
        from test_wework_edit1.page.add_contact.add_contact_manual.contactaddpage import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        toast = self.find(self.text_ele).text
        return toast

    def add_list(self):
        '''
        通过通讯录添加
        :return:
        '''
        # 点击从微信添加人员

        self.find_and_click(self.list_element)
        return ContactListAddPage(self.driver)
