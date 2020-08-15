import pytest

from pythoncode.calculator import calculator
'''
pytest命名规则：
文件名：test开头（test_*.py)
类名：Test开头
方法名：test_开头
'''

class Testcalc:
    def setup_class(self):
        print("setup:开始计算")
        self.calc = calculator()

    def teardown_clss(self):
        print("teardown:计算结束")
        self.calc = calculator()

    # @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',
                             [
                                 (0,1,1),
                                 (0.1,2,2.1),
                                 (101,99,200),
                                 (0,-1,-1),
                                 # (0,1,1),
                                 # (0,1,1),
                             ])
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
                             ])
    def test_div(self,a,b,expect):
        '''
        测试相除
        '''
        print("测试相除")
        # calc = calculator()
        result = self.calc.div(a,b)
        assert expect == result
