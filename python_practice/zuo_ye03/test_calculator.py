import pytest
import yaml

from python_practice.zuo_ye03.calculator import Calculator1

with open("calc02.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']['add_datas']
    print(add_datas)
    add_myid = datas['add']['add_myid']
    print(add_myid)
    div_datas = datas['div']['div_datas']
    print(div_datas)
    div_myid = datas['div']['div_myid']
    print(div_myid)


class TestCalc:

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator1()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize(
        "a0,b0,expect0",
        add_datas, ids=add_myid

    )
    def test_add(self, a0, b0, expect0):
        add_result = self.calc.add(a0, b0)
        if isinstance(add_result, float):
            add_result = round(add_result, 2)
        assert add_result == expect0

    @pytest.mark.parametrize(
        "a1,b1,expect1",
        div_datas, ids=div_myid

    )
    def test_div(self, a1, b1, expect1):
        div_result = self.calc.div(a1, b1)
        if isinstance(div_result, float):
            div_result = round(div_result, 2)
            if a1 == 0:
                print("a不能为0")
                return
        assert div_result == expect1
