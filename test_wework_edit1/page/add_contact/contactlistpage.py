from appium.webdriver.common.mobileby import MobileBy

from test_wework_edit1.page.add_contact.addmemberpage import AddMemberPage
from test_wework_edit1.page.basepage import BasePage
from test_wework_edit1.page.del_contact.searchpage import SearchPage


class ContactListPage(BasePage):
    '''
    在通讯录  添加人员/查询
    '''
    addmember_text = "添加成员"
    search_button = (MobileBy.ID, "com.tencent.wework:id/h9z")

    def add_contact(self):
        # 滚动查找"添加成功"元素
        self.find_scroll(self.addmember_text).click()

        return AddMemberPage(self.driver)

    def search_contact(self):
        # 点击 搜索框
        self.find_and_click(self.search_button)
        return SearchPage(self.driver)
