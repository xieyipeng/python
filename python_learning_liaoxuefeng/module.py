# -*- coding: utf-8 -*-

' a test module '
from PIL import Image

__author__ = 'xieyipeng'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('icon,world')
    elif len(args) == 2:
        print('icon,%s' % args[1])
    else:
        print('too many arguments!')


# 作用域：
# _xxx前缀代表private


if __name__ == '__main__':
    test()

im = Image.open('icon/test.png')
print(im.format, im.size, im.mode)

print(sys.path)


# 面向对象编程
# 加__变成private
# 双下划线开头结尾，特殊变量，可直接访问

class Student(object):  # object 表示该类从哪个类继承下来的
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('xieyipeng', 88)

print(bart)
print(Student)

bart.print_score()
print(bart.get_grade())
print(bart._Student__name)  # 即使是__xxx之类的变量依旧可以访问
