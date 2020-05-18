'''文本词频统计
需求：一篇文章，出现了哪些词？哪些词出现最多
该怎么做？英文文本：Hamlet 分析词频
https://python123.io/resources/pye/hamlet.txt '''


def getText():  # 获得文本
    txt = open("hamlet.txt", "r").read()  # 打开hamlet文件
    txt = txt.lower()  # 避免大小写的干扰
    for ch in '~!@#$%^&*()_+-=[]{}\|;:",./<>?':  # 除去各种特殊符号，用空格代替
        txt = txt.replace(ch, " ")  # 字符串替换函数
    return txt


hamletTxt = getText()
words = hamletTxt.split()  # 字符串中，.split默认用空格分隔文本，以列表形式返回给变量
counts = {}  # 单词和出现次数之间形成映射，构建字典类型，定义空字典
for word in words:
    counts[word] = counts.get(word, 0) + 1
# 对每个单词进行统计，假设将单词保存在变量word中，使用一个字典类型counts={}，统计单词出现的次数。
# 字典类型的counts.get(word,0)方法表示：如果word在counts中，则返回word对应的值，
# 如果word不在counts中，则返回0

items = list(counts.items())  # 将字典的所有键值对转换为列表类型
items.sort(key=lambda x: x[1], reverse=True)
# 对列表类型排序，默认排序从小到大；reverse=True 次数从大到小
# lambda在该代码中相当于：
# def func(x):
#      return (x[1])
# 该函数是将列表里每个元素的第二项，也是出现次数作为排序依据

for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
