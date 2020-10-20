#coding:utf-8
'''
学习raise手动设置异常
'''

# v1.0 简单的实现
# a = input('please enter a number:')
# if not a.isnumeric():
#     print('输入的不是数字')

# v2.0 使用raise，人为抛出ValueError
# a = input('please enter a number:')
# if not a.isnumeric():
#     raise ValueError("必须是数字")

# V2.1 使用try except处理异常
try:
    a = input('please enter a number:')
    if not a.isnumeric():
        raise ValueError("必须是数字")
except ValueError as e:
    print("引发了异常：",repr(e))