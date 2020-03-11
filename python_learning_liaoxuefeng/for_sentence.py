# ************循环************
# python的循环有两种
# 1、
classmates = ['michael', 'bob', 'tracy']
for name in classmates:
    print(name)

# 累加
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# range()函数和list()函数：
print(list(range(5)))  # [0, 1, 2, 3, 4]

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 2、while循环：
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
