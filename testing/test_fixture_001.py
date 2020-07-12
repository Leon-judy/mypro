import pytest


# fixture scope = 默认，test_fixture_001.py
class TestLogin1:

    def test_1(self, login1):
        print("用例", login1)

    @pytest.mark.parametrize("login1", ["user4", "user5"], indirect=True)
    def test_2(self, login1):
        print("用例", login1)

    @pytest.mark.parametrize("login2", ["user4", "user5"], indirect=True)
    def test_3(self, login2):
        print("用例", login2)
