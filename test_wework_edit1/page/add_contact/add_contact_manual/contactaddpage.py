from appium.webdriver.common.mobileby import MobileBy

from test_wework_edit1.page.add_contact.addmemberpage import AddMemberPage
from test_wework_edit1.page.basepage import BasePage


class ContactAddPage(BasePage):
    name_ele = (MobileBy.ID, "com.tencent.wework:id/awt")
    phone_ele = (MobileBy.ID, "com.tencent.wework:id/f1e")
    group_ele = (MobileBy.XPATH, "//*[@text='设置部门']")
    confirm_ele = (MobileBy.ID, "com.tencent.wework:id/g09")
    save_ele = (MobileBy.ID, "com.tencent.wework:id/h9w")

    def set_name(self, name):
        # 设置姓名
        self.find_and_sendkeys(self.name_ele, name)
        return self

    def set_phone(self, phone):
        # 设置手机号
        self.find_and_sendkeys(self.phone_ele, phone)
        return self

    def set_group(self):
        # 点击确定
        self.find_and_click(self.group_ele)
        self.find_and_click(self.confirm_ele)
        return self

    def click_save(self):
        # 点击“保存”
        self.find_and_click(self.save_ele)
        return AddMemberPage(self.driver)
