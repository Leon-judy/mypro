import pytest
import sys

sys.path.append('..')
from pythoncode.calc import Calculator


def setup_module():
    print("模块级别 setup")


def teardown_module():
    print("模块级别 teardown")


def setup_function():
    print("函数级别 setup")


def teardown_function():
    print("函数级别 teardown")


def test_func_add1():
    assert 1 == 1


class TestCalc(object):
    def setup_class(self):
        # cal实例化后 为setup里面的局部变量，
        # 前面加一个self.就变成实例变量，
        # 可以在其他的方法里面调用
        self.cal = Calculator()
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    # def setup(self):
    #     print("set up")
    #
    # def teardown(self):
    #     print("teardown")

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, result', [
        (1, 1, 2),
        (2, 2, 4),
        (4.1, 4.1, 8.2),
        (5.5, 5.5, 11)
    ], ids=['int', 'int', 'float', 'float'])
    def test_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    @pytest.mark.add
    def test_add1(self, login):
        print("yield :", login)  # 把yield return的值打印出来
        assert 4 == self.cal.add(2, 2)

    @pytest.mark.div
    def test_div(self):
        assert 1 == self.cal.div(2, 2)
        print("abc")
        # print(sys.path)

    @pytest.mark.div
    def test_div1(self, login):
        assert 2 == self.cal.div(4, 2)
        print("def")
        # print(sys.path)


class TestTwo(object):
    def test_one(self):
        print("TestTwo::test_one !!!")

    def test_two(self):
        print("TestTwo::test_two !!!")
