#coding:utf-8
'''
测试tmp
'''

from pytest import ExitCode

def test_needsfile(tmpdir):
    print(tmpdir)
    assert 1

def test_failurecase():
    assert 0

def test_pass_one():
    assert 1

def test_failure_one():
    assert 0

def test_pass_two():
    assert 1