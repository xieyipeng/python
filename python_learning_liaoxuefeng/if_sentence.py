# ************条件判断************
age = 3
if age >= 18:
    print('your age is', age)  # 逗号相当于空格
    print('adult')
# print('123','456')
# print('123'+'456')
else:
    print('your age is', age)
    print('teenager')

# elif 语句
age = 3
if age >= 18:
    print('adult')
elif age >= 6:  # elif是else if的缩写
    print('teenager')
else:
    print('kid')

# 再议input
s = input('birth:\n')  # input返回值类型为str
birth = int(s)  # 强制转换
if birth < 2000:
    print('00前')
else:
    print('00后')
