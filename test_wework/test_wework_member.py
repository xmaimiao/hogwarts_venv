import re
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

with open("./addmember1.yaml") as f:
    adddatas1 = yaml.safe_load(f)
    addids1 = adddatas1.keys()
    adddata1 = adddatas1.values()

with open("./addmember2.yaml") as f:
    adddatas2 = yaml.safe_load(f)
    addids2 = adddatas2.keys()
    adddata2 = adddatas2.values()

with open("./delmember.yaml") as f:
    deldatas = yaml.safe_load(f)
    delids = deldatas.keys()
    deldata = deldatas.values()


class TestWeWork:
    def setup(self):
        caps = {}
        caps["platformName"] = 'Android'
        caps["deviceName"] = '127.0.0.1:7555'
        caps["platformVersion"] = '6.0.1'
        caps["appPackage"] = 'com.tencent.wework'
        caps["automationName"] = 'uiautomator2'
        caps["appActivity"] = '.launch.WwMainActivity'
        caps["noReset"] = 'true'
        # caps['settings[waitForIdleTimeout]'] = 0
        # 启动之前不关闭APP
        caps["dontStopAppOnReset"] = 'true'
        caps["skipDeviceInitializati"] = 'true'
        # caps["unicodeKeyboard"] = 'true'
        # caps["resetKeyboard"] = 'true'
        caps["chromedriverExecutable"] = 'C:\Program Files (x86)\Appium\chromedriver2.20.exe'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        pass

    @pytest.mark.parametrize("name", adddata1, ids=addids1)
    def test_addmember1(self, setting, name):

        """
        1.打開企業微信首頁
        2.點擊 通訊錄
        3.滾動查找並點擊 添加成功
        4.點擊 從微信通訊錄中添加
        5.滾動查找xxx，點擊  添加
        6.验证已加入該人員
        :return:
        """
        # 点击通讯录
        index_ele = (MobileBy.XPATH, '//*[@text="通讯录"]')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(index_ele))
        self.driver.find_element(*index_ele).click()

        # 滚动查找"添加成功"元素
        button_ele = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                                            '.scrollable(true).instance(0))'
                                                                            '.scrollIntoView(new UiSelector()'
                                                                            '.text("添加成员").instance(0));')
        # 获取通讯录人数
        if "人未加入" in self.driver.page_source:
            member_text_before = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"人未加入")]').text
            member_before = int(re.search("\w(\d{1,3})", member_text_before).group(1))
        else:
            print(self.driver.page_source)
            member_before = 0

        # 点击“添加人员”按钮
        button_ele.click()

        # 点击从微信添加人员
        self.driver.find_element(MobileBy.XPATH, '//*[@text="从微信/手机通讯录中添加"]').click()
        # 滾動查找人员，點擊  添加
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
        f'text("{name}").instance(0));')
        member_ele = (MobileBy.XPATH, f"//*[@text='{name}']/../../../..//*[@text='添加']")
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(member_ele))
        self.driver.find_element(*member_ele).click()
        sleep(3)
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']/../../../*[@text='加入企业通讯录']").click()
        self.driver.back()
        self.driver.back()

        # 验证添加人员成功
        text = member_before
        ele = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                                     'scrollable(true).instance(0)).'
                                                                     'scrollIntoView(new UiSelector().'
        f'text("添加成员").instance(0));')
        sleep(2)
        member_text_after = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"人未加入")]').text
        member_after = int(re.search("\w(\d{1,3})", member_text_after).group(1))

        assert member_after - 1 == member_before

    @pytest.mark.parametrize("data", adddata2, ids=addids2)
    def test_addmember2(self, setting, data):

        """
        從“手動添加人員”添加
        :param self:
        :return:
        """
        # 处理data参数
        name = data['name']
        phone = data['phone']

        # 点击打开 通讯录
        index_ele = (MobileBy.XPATH, '//*[@text="通讯录"]')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(index_ele))
        self.driver.find_element(*index_ele).click()

        # 滚动查找"添加成功"元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector()'
                                                               '.text("添加成员").instance(0));').click()

        # 点击 “手动添加人员”
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入姓名和手机号
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/awt").send_keys(name)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f1e").send_keys(phone)
        # 点击设置部门
        self.driver.find_element(MobileBy.XPATH, "//*[@text='设置部门']").click()
        # 点击确定
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g09").click()
        # 点击“保存”
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h9w").click()
        # 验证添加成功
        toast = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'添加成功')]").text
        self.driver.back()

        assert "添加成功" in toast

    @pytest.mark.parametrize("name", deldata, ids=delids)
    def test_delmember(self, setting, name):
        """
        1.打开企业微信，点击 通讯录
        2.滚动定位到人员xxx，点击人员
        3.点击右上角设置符号
        4.点击 编辑成员
        5.点击 删除成功
        :return:
        """

        # 点击通讯录
        index_ele = (MobileBy.XPATH, '//*[@text="通讯录"]')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(index_ele))
        self.driver.find_element(*index_ele).click()

        # 滚动查找底部"添加人员"元素,获取通讯录人数
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector()'
                                                               '.text("添加成员").instance(0));')
        if "人未加入" in self.driver.page_source:
            member_text_before = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"人未加入")]').text
            member_before = int(re.search("\w(\d{1,3})", member_text_before).group(1))
        else:
            return

        print(name)

        # 滚动定位到人员xxx，点击人员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector()'
        f'.text("{name}").instance(0));').click()

        # 点击右上角设置符号
        index_ele = (MobileBy.ID, 'com.tencent.wework:id/h9p')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(index_ele))
        self.driver.find_element(*index_ele).click()
        # 点击 编辑成员
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/b2c').click()
        # 点击 删除成功
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/e3f').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/bci').click()
        sleep(3)
        # 验证删除人员成功
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector()'
                                                               '.text("添加成员").instance(0));')
        if member_before > 2:
            member_text_after = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"人未加入")]').text
            member_after = int(re.search("\w(\d{1,3})", member_text_after).group(1))
            assert member_after + 1 == member_before
        else:
            assert "人未加入" not in self.driver.page_source


if __name__ == '__main__':
    pytest.main()
