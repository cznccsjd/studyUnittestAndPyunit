#coding:utf-8

import unittest

class BasicExample(unittest.TestCase):
    def setUp(self):
        print("This is function:setUp")

    def test_upper(self):
        print('function:test_upper')
        self.assertEqual('Foo'.upper(), 'FOO')

    def test_isupper(self):
        print('function:test_isupper')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print('function:test_split')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split() fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
        print('this is function:tearDown\n')

if __name__ =='__main__':
    unittest.main()