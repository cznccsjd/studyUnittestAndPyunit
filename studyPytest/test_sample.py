#coding:utf-8

'''
pytest官方学习的第一个样例
'''


def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5