'''获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。

输入:Alice-Bob-Charis-David-Eric-Flurry	
输出:Alice+Flurry

s.split(k)以k为标记分割s，产生一个列表。通过该题目，掌握split()方法的使用，注意：k可以是单字符，也可以是字符串。'''


s = input()
ls = s.split("-")
print("{}+{}".format(ls[0], ls[-1]))