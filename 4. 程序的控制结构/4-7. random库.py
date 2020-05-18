import random

# random生成[0.0 1.0)之间的随机小数
print(random.random())

# randint(a,b) 生成一个[a,b]之间的随机整数
print(random.randint(1, 10))

# uniform(a,b) 生成一个[a,b]之间的随机小数
print(random.uniform(1, 10))

# randrange(start,stop,[,step]) 生成一个[start,stop)之间以step为步长的随机整数
print(random.randrange(0, 100, 4))

# choice(seq) 从序列类型，例如列表中随机返回一个元素
print(random.choice(range(100)))

ls = list(range(10))
print(ls)
# shuffle(seq) 将序列类型中的元素随机排列，返回打乱后的序列
random.shuffle(ls)
print(ls)

# 生成随机数之前可以通过seed()函数指定随机数种子，随机数种子一般是一个整数，
# 只要种子相同，每次生成的随机数序列也相同。这种情况便于测试和同步数据，例如：
random.seed(125)
print("{}.{}.{}".format(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))
print("{}.{}.{}".format(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))
random.seed(125)
print("{}.{}.{}".format(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))

# 随机生成100内的10个整数
for i in range(10):
    print(random.randint(0,100))

# 随机选取0到100之间的整数
print(random.randint(1,100,2))

# 从字符串'abcdefghij'中随机选取四个字符
s='abcdefghij'
for i in range(4):
    print(s[random.randint(0,len(s)-1)])

# 随机选取列表['apple','pear','peach','orange']中的一个字符
print(['apple','pear','peach','orange'][random.randint(0,3)])
