import pytest


# scope="session"
@pytest.fixture()
def login():
    print("输入账号密码：")
    yield ['username', 'passworld']
    print('清理数据完成')


users = ["user1", "user2", "user3"]


# scope="module"
@pytest.fixture(params=users)
def login1(request):
    print("输入账号密码：")
    yield request.param
    print('清理数据完成')


@pytest.fixture()
def login2(request):
    print("输入账号密码：")
    yield request.param
    print('清理数据完成')


@pytest.fixture(autouse=True)
def set():
    print("开始计算")
    yield
    print("计算结束")
