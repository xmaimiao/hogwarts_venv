from typing import List
import pytest
import yaml
from _pytest.python import Metafunc


@pytest.fixture(scope='module')
def calcu_m():
    print("【——>開始計算】")
    yield
    print("【——>結束計算】")


# 動態生成測試用例
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.mydatas, ids=metafunc.module.myids,
                             scope='function')


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='The environment attributes.')


# 自定義改變測試環境
@pytest.fixture(scope='session')
def getenv(request):
    myenv = request.config.getoption('--env', default='test')
    if myenv == 'test':
        datapath = './test/data.yaml'

    elif myenv == 'dev':
        datapath = './dev/data.yaml'

    elif myenv == 'st':
        datapath = './st/data.yaml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas
