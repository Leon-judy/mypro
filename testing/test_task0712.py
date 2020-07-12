import pytest
import sys

sys.path.append('..')
from pythoncode.calc import Calculator


class TestCalc(object):

    def setup_class(self):
        self.c = Calculator()

    @pytest.mark.parametrize('a, b, result', [
        (10, 50, 60),
        (0.009, 0.007, 0.02)], ids=["int", "float"])
    def test_add(self, a, b, result):
        assert str(result) == self.c.add(a, b)

    @pytest.mark.parametrize('a, b, result', [
        (10, 50, -40),
        (0.009, 0.333, -0.32)], ids=["int", "float"])
    def test_sub(self, a, b, result):
        assert str(result) == self.c.sub(a, b)

    @pytest.mark.parametrize('a, b, result', [
        (10, 50, 500),
        (99, 0.333, 32.97)], ids=["int", "float"])
    def test_mul(self, a, b, result):
        assert str(result) == self.c.mul(a, b)

    @pytest.mark.parametrize('a, b, result', [
        (50, 10, 5),
        (10, 3, 3.33)], ids=["int", "float"])
    def test_div(self, a, b, result):
        assert str(result) == self.c.div(a, b)
