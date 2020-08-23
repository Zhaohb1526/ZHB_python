import pytest

#一个方法上面加上@pytest.fixture()装饰器，就变为了fixture方法
@pytest.fixture()
def figure():
    print("计算")

def test_add():
    print("输入数字")