#coding:utf-8

'''
断言代码引发的异常
'''

import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()