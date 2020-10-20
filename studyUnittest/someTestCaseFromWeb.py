#coding:utf-8
'''
各个学习文档上，抄来的学习用例
'''

import unittest

class NumberTest(unittest.TestCase):
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        :return:
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)