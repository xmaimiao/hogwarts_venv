from _pydecimal import Decimal, getcontext

import pytest
import yaml

'''課後作業2.1：類TestCalc1按照【加-減-乘-除】順序執行用例'''

with open("./datas2_2.yaml") as f:
    datas = yaml.safe_load(f)
    mydatas = datas.values()
    myids = datas.keys()


class TestCalc1:

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect", [(0, 20, 0), (5, 0, 0)])
    def test_div1(self, a, b, expect):
        try:
            assert expect == a / b
        except Exception as e:
            print(e)
            raise e

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", [(10, 20, 200), (-5, 6, -30)])
    def test_mult1(self, a, b, expect):
        assert expect == a * b

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", [(20, 20, 0), (5, 6, -1)])
    def check_sub1(self, a, b, expect):
        assert expect == a - b

    @pytest.mark.run(order=1)
    def test_add1(self, param, calcu_m):
        assert param[2] == param[0] + param[1]


if __name__ == '__main__':
    pytest.main()
