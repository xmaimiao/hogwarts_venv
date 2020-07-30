from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from test_wework_edit1.page.basepage import BasePage


class ContactListAddPage(BasePage):
    '''
    從微信通訊錄添加
    '''
    def weworkadd(self, name):
        # 滾動查找人员，找到“添加”按鈕
        self.find_scroll(name)
        member_ele = (MobileBy.XPATH, f"//*[@text='{name}']/../../../..//*[@text='添加']")

        # 點擊“添加”按鈕
        self.webdriver_wait(member_ele)
        self.find_and_click(member_ele)
        sleep(3)

        # 點擊“加入企業通訊錄”按鈕
        addlist_ele = (MobileBy.XPATH, f"//*[@text='{name}']/../../../*[@text='加入企业通讯录']")
        self.find_and_click(addlist_ele)

        # 獲取添加成功 結果 返回
        added_ele = (MobileBy.XPATH, f"//*[@text='{name}']/../../../*[@text='已加入']")
        result = self.find(added_ele).text

        return result
