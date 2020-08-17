import pytest
import yaml

from pythoncode.calculator import calculator
'''
pytest命名规则：
文件名：test开头（test_*.py)
类名：Test开头
方法名：test_开头
'''

#读取测试数据
def get_datas():
    with open('./datas/calculator.yml',encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas,myids]


class Testcalc:
    def setup_class(self):
        print("setup:开始计算")
        self.calc = calculator()

    def teardown_class(self):
        print("teardown:计算结束")
        self.calc = calculator()

    # @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',get_datas()[0],ids=get_datas()[1])
    def test_add(self,a,b,expect):
        '''
        测试相加
        '''
        print("测试相加")
        # calc = calculator()
        result = self.calc.add(a,b)
        assert expect == result



    @pytest.mark.parametrize('a,b,expect',
                             [
                                 (0,1,0),
                                 (0.1,2,0.05),
                                 (101,10,10.1),
                                 (0,-1,0),
                                 # (0,1,1),
                                 # (0,1,1),
                             ],ids=['整数',  '小数', '大数', '零'])
    def test_div(self,a,b,expect):
        '''
        测试相除
        '''
        print("测试相除")
        # calc = calculator()
        result = self.calc.div(a,b)
        assert expect == result
