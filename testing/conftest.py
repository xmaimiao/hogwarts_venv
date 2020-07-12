import pytest


@pytest.fixture(scope='module')
def calcu_m():
    print("【——>開始計算】")
    yield
    print("【——>結束計算】")
