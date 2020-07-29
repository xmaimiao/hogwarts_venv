from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from test_wework_edit1.page.basepage import BasePage
from test_wework_edit1.page.del_contact.infomationpage import InformationPage
from test_wework_edit1.page.context import Context


class SearchPage(BasePage):
    name_element = (MobileBy.ID, "com.tencent.wework:id/fxc")

    def get_contact(self, name):
        '''
        查询关键字，获取结果
        :param name:
        :return:
        '''
        # 获取联系人列表
        sleep(3)
        result_after = self.find_eles((MobileBy.XPATH, f"//*[@text='{name}']"))
        return result_after

    def personal_infor(self, name):
        '''
        判断是否存在联系人，存在则进入下一步
        :param name:
        :return:
        '''
        self.find_and_sendkeys(self.name_element, name)
        sleep(3)
        elelist = self.find_eles((MobileBy.XPATH, f"//*[@text='{name}']"))
        setattr(Context, "result_before", elelist)
        if len(elelist) < 2:
            print("没有这个联系人")
            return
        else:
            elelist[1].click()
            sleep(3)
            return InformationPage(self.driver)
