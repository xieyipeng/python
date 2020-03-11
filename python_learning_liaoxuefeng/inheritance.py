# 继承
from types import MethodType


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Eating fish...')


dog = Dog()
dog.run()
cat = Cat()
cat.run()


# 动态语言vs静态语言：
# java之类的静态语言，传入的必须是Animal类型或其子类，但是对于
# python之类的动态语言，只要传入的对象有一个run方法即可（动态语言的鸭子类型）
def run_twice(animal):
    animal.run()


run_twice(Animal())
run_twice(dog)
run_twice(cat)

# 获取对象信息
# type()
print(type(1234))


# instance()函数

# 获得对象的所有方法和属性：dir()

# class Student(object):
#     name = 'Student'  # 类属性

class Student(object):
    pass


# s = Student()
# print(s.name)
#
# s.name = 'xieyipeng'
# print(s.name)
# del s.name
# print(s.name)

# 面向对象高级编程：
# 多重继承，定制类，元类

# 使用__slots__


# 绑定方法：
def set_age(self, age):
    self.age = age


s = Student()

s.name = 'xieyipeng'
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


# 在程序运行过程中给类绑定方法：

def set_score(self, score):
    self.score = score


Student.set_score = MethodType(set_score, Student)


# __slots__:

class StudentTest(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


# 使用@property：技能检查参数，又能用类似属性这样简单的方式访问类的变量

# 多重继承：

class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class Bat(Animal, FlyableMixIn):
    pass
