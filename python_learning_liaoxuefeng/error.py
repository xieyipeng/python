# 错误信息


# from absl import logging
#
#
# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def ma():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
#
# ma()
# print('END')

# 断言：
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
#
# def ma():
#     foo('0')
#
#
# ma()

# logging
import logging

logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10 / n


def ma():
    foo('0')


ma()
"""
if __name__ == '__main__':
if __name__ == '__main__'的意思是：当.py文件被直接运行时，
if __name__ == '__main__'之下的代码块将被运行；当.py文件以
模块形式被导入时，if __name__ == '__main__'之下的代码块不
被运行。
"""

