#coding:utf-8

'''
直接测试类，类需要以Test打头，否则会被忽略
类下的方法，需要以约定的test_*格式编写，不然也会被忽略
'''

class TestClass():
    def test_one(self):
        x = "hello"
        assert "o" in x

    def two_test(self):
        x = "hello"
        assert "e" in x

    def three_test_case(self):
        x = "hello"
        assert "b" in x

class TestClassTwo():
    def test_two_one(self):
        x = "hello"
        assert "s" in x

class ClassThreeTest():
    def test_three_one(self):
        x = "hello"
        assert "e" in x