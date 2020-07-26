import pytest


@pytest.fixture(scope='module')
def setting():
    print("【——>开始添加/删除通讯录人员】")
    yield
    print("【——>結束添加/删除通讯录人员】")
