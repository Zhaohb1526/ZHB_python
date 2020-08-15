#setup_module、teardown_module整个模块执行前后分别被调用一次
# def setup_module()
#     print("setup:模块级别")
#
#
# def teardown_module()
#     print("teardown:模块级别")

def setup_function()
    print("setup:函数级别")

def teardown_function()
        print("teardown:函数级别")

def test_case()
    print("case")

class Testcalc1:
    # setup_class、teardowd_class为类级别，在每个类的执行前后分别被调用一次
    def setup_class(self):
        print("setup_class:1类级别")

    def teardowd_class(self):
        print("teardowd_class:1类级别")

    # setup、teardown为方法级别，在每个类里的测试用例前后分别被调用一次
    def setup(self):
        print("setup：开始计算")

    def teardown(self):
        print("teardown：计算结束")

    def test_a(self):
        print("testa")

    def test_b(self):
        print("testb")


# class Testcalc2:
#     # setup_class、teardowd_class为类级别，在每个类的执行前后分别被调用一次
#     def setup_class(self):
#         print("setup_class:类级别")
#
#     def teardowd_class(self):
#         print("teardowd_class:类级别")
#
#     # setup、teardown为方法级别，在每个类里的测试用例前后分别被调用一次
#     def setup(self):
#         print("setup：开始计算")
#
#     def teardown(self):
#         print("teardown：计算结束")
#
#     def test_a(self):
#         print("testa")
#
#     def test_b(self):
#         print("testb")
