import MineOs, django

MineOs.environ.setdefault("DJANGO_SETTINGS_MODULE", "induction.settings")  # project_name 项目名称
django.setup()
# 枚举类：
from enum import Enum, unique

from django.db.models import Model, IntegerField
from google.protobuf.internal.descriptor_pool_test import StringField

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Mov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '->', member, ',', member.value)


# 更精确控制枚举类型：

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sta = 6


# 元类：
# type():--查看一个类型或变量的类型
# 用type()函数创建Hello类
def fn(self, name='world'):
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # class名称 + 父类集合 + class方法名与函数名绑定

h = Hello()
print(h.hello())


# metaclass:元类--创建类的类

class ListMetaClass(type):  # metaclass是类的模板，必须从type派生
    def __new__(cls, name, bases, attrs, *args, **kwargs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaClass):
    pass


L = MyList()
L.add(1)
print(L)


# 普通的list没有add方法
# L2=list()
# L2.add(1)
# print(L2)

# 编写ORM对象-关系映射框架：

class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 实现ORM框架：
class Field(object):  # 保存数据库的字段名和字段类型
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '%s:%s' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs, *args, **kwargs):
        if name == 'xieyioeng':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.item():
            if isinstance(v, Field):
                print('Found mapping : %s -> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mapping__.item():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'INSERT INTO %s(%s) VALUES (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


u = User(id=12345, name='xieyipeng', email='3239303719@qq.com', password='12345')
u.save()
