import pytest
import yaml

'''課後作業2.2：類TestCalc2減法依賴加法，除法依賴乘法'''

with open("./datas2_2.yaml") as f:
    datas = yaml.safe_load(f)
    mydatas = datas.values()
    myids = datas.keys()


class TestCalc2:

    # 目前check_add2涉及多組測試數據，僅以最後一組測試數據結果作為test_sub2執行/跳過的依據
    @pytest.mark.dependency(name="check_add2")
    def check_add2(self, param, calcu_m):
        assert param[2] == param[0] + param[1]

    @pytest.mark.dependency(depends=["check_add2"])
    @pytest.mark.parametrize("a,b,expect", [(20, 20, 0), (5, 6, -1)], ids=["data1", "data2"])
    def test_sub2(self, a, b, expect):
        assert expect == a - b

    @pytest.mark.dependency(name="test_mult2")
    @pytest.mark.parametrize("a,b,expect", [(10, 20, 200), (-5, 6, -30)], ids=["data1", "data2"])
    def test_mult2(self, a, b, expect):
        assert expect == a * b

    @pytest.mark.dependency(depends=["test_mult2"])
    @pytest.mark.parametrize("a,b,expect", [(0, 20, 0), (5, 0, 0)], ids=["data1", "data2"])
    def test_div2(self, a, b, expect):
        try:
            assert expect == a / b
        except Exception as e:
            print(e)
            raise e


if __name__ == '__main__':
    pytest.main()
