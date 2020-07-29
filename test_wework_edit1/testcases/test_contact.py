import pytest
import yaml
from test_wework_edit1.page.context import Context
from test_wework_edit1.page.app import App

with open("../data/addmember1.yaml") as f:
    adddatas1 = yaml.safe_load(f)
    addids1 = adddatas1.keys()
    adddata1 = list(adddatas1.values())

with open("../data/addmember2.yaml") as f:
    adddatas2 = yaml.safe_load(f)
    addids2 = adddatas2.keys()
    adddata2 = adddatas2.values()

with open("../data/delmember.yaml") as f:
    deldatas = yaml.safe_load(f)
    delids = deldatas.keys()
    deldata = deldatas.values()


class TestContact:

    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back(5)

    @pytest.mark.parametrize("data", adddata2, ids=addids2)
    def test_addcontact(self, data):
        '''
        验证手动添加联系人
        :return:
        '''
        # 处理data参数
        name = data['name']
        phone = data['phone']

        mypage = self.main.goto_contactlist(). \
            add_contact().add_menual(). \
            set_name(name).set_phone(phone). \
            set_group().click_save()
        text = mypage.get_toast()
        assert "成功" in text

    @pytest.mark.parametrize("name", deldata, ids=delids)
    def test_delcontact(self, name):
        '''
        验证删除联系人
        :param name:
        :return:
        '''
        result_after = self.main.goto_contactlist(). \
            search_contact().personal_infor(name). \
            person_setting().contactedit(). \
            contactdelpage().get_contact(name)
        result_before = getattr(Context, "result_before")
        assert len(result_before) - 1 == len(result_after)

    @pytest.mark.parametrize("name", adddata1, ids=addids1)
    def test_listaddcontact(self, name):
        '''
        验证通过通讯录添加人员
        :return:
        '''
        result = self.main.goto_contactlist(). \
            add_contact().add_list(). \
            weworkadd(name)
        assert "已加入" in result
