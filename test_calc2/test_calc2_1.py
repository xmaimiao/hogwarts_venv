from _pydecimal import Decimal, getcontext

import pytest
import yaml

'''課後作業1.1：使用參數化數據驅動，自動生成用例
   課後作業1.2：修改用例為check_開頭，修改測試用例的執行規則，執行所有check_、test_開頭的測試用例'''

with open("./datas2_1.yaml") as f:
    datas = yaml.safe_load(f)
    addatas = datas["add"].values()
    addids = datas["add"].keys()

    subdatas = datas["sub"].values()
    subids = datas["sub"].keys()

    multdatas = datas["mult"].values()
    multids = datas["mult"].keys()

    divdatas = datas["div"].values()
    divids = datas["div"].keys()


class TestCalc:
    getcontext().prec = 10

    @pytest.mark.parametrize("data", addatas, ids=addids)
    def check_add(self, data, calcu_m):
        c = Decimal(str(data["a"])) + Decimal(str(data["b"]))
        assert c == Decimal(str(data["expect"]))

    @pytest.mark.parametrize("data", subdatas, ids=subids)
    def check_sub(self, data):
        c = Decimal(str(data["a"])) - Decimal(str(data["b"]))
        assert c == Decimal(str(data["expect"]))

    @pytest.mark.parametrize("data", multdatas, ids=multids)
    def test_mult(self, data):
        c = Decimal(str(data["a"])) * Decimal(str(data["b"]))
        assert c == Decimal(str(data["expect"]))

    @pytest.mark.parametrize("data", divdatas, ids=divids)
    def test_div(self, data):
        try:
            c = Decimal(str(data["a"])) / Decimal(str(data["b"]))
            assert c == Decimal(str(data["expect"]))
        except Exception as e:
            print(e)
            raise e


if __name__ == '__main__':
    pytest.main()
