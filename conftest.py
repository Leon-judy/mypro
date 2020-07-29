from typing import List

import pytest

# scope="session"
import yaml


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
    print("输入账号密码：", request)
    yield request.param
    print('清理数据完成')


# autouse=True
@pytest.fixture()
def set():
    print("开始计算")
    yield
    print("计算结束")


# 解决参数化时，出现中文乱码的问题
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # items.reverse()  # 倒序
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)


def pytest_addoption(parser):  # parser解析器
    mygroup = parser.getgroup("hogwarts")  # 设置一个group结点
    # 在该结点下添加一个想要的参数
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='testcases',
                      dest='env',  # 加入一个环境的标识
                      help='set your run env'
                      )
    mygroup.addoption("--env1",  # 注册一个命令行选项
                      default='testcases',
                      dest='env1',
                      help='set your run env'
                      )


# 处理命令行传来的参数，设置成fixture，将test环境和dev环境或者其它环境
# 分别处理，获取想要的不同环境下的测试数据
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='testcases')
    print("输入的ENV:", myenv)
    if myenv == 'testcases':
        datapath = 'data/testcases/data.yml'

    if myenv == 'dev':
        datapath = 'data/dev/data.yml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas
