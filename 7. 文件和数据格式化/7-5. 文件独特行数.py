'''统计附件文件中与其他任何其他行都不同的行的数量，即独特行的数量。

如果需要"去重"功能，请使用集合类型。
ls.remove()可以去掉某一个元素，如果该行是独特行，去掉该元素后将不在集合t中出现。

如果需要"去重"功能，请使用集合类型。
ls.remove()可以去掉某一个元素，如果该行是独特行，去掉该元素后将不在集合t中出现。'''

f = open("7-5. latex.log")
ls = f.readlines()
s = set(ls)
for i in s:
    ls.remove(i)
t = set(ls)
print("共{}独特行".format(len(s)-len(t)))
