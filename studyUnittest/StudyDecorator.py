#coding:utf-8
'''
装饰器学习文件
'''
'''
# 不能运行
from time import ctime, sleep

def record_time(func):
    print('[%s] %s() called.'% (ctime(), func.__name__))
    return func()

# @record_time
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    foo()
'''
'''
def Hi(name='jack'):
    def greet():
        print("Hi, %s"% name)
    def welcome():
        print("welcome")

    if name == 'jack':
        return greet
    else:
        return welcome

a = Hi()
print(a())
'''

'''
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return ("Function is running")

can_run = True
print(func())
'''

'''
没能运行起来
import unittest
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1,3), "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the libraty
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
            # test code that depends on the external resource
            pass
'''