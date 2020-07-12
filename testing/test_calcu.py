import pytest
import yaml
from decimal import *
from testing.usual import usual


class TestAdd:

    @pytest.mark.parametrize("data", yaml.safe_load(open("./data_add.yaml")),
                             ids=['1.int', '2.float', '3.int+float', '4.before=0', '5.after=0', '6.be/af=0'])
    def test_add(self, data, calcu_m):
        usual(data, '+')

    @pytest.mark.parametrize("data", yaml.safe_load(open("./data_sub.yaml")),
                             ids=['1.int,be>af', '2.float,be>af', '3.float-int,be>af',
                                  '4.int,be<af', '5.float,be<af', '6.float-int,be<af',
                                  '7.int,be=af', '8.float,be=af',
                                  '9.before=0', '10.after=0', '11.be/af=0'])
    def test_sub(self, data):
        usual(data, '-')

    @pytest.mark.parametrize("data", yaml.safe_load(open("./data_mult.yaml")),
                             ids=['1.int', '2.float', '3.int*float', '4.before=0', '5.after=0', '6.be/af=0'])
    def test_mult(self, data):
        usual(data, '*')

    @pytest.mark.parametrize("data", yaml.safe_load(open("./data_div.yaml")))
    def test_div(self, data):
        usual(data, '/')


if __name__ == '__main__':
    pytest.main()
