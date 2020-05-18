'''完成如下功能：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
获得用户输入数字N，计算并输出从N开始的5个质数，单行输出，质数间用逗号,分割。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
注意：需要考虑用户输入的数字N可能是浮点数，应对输入取整数；最后一个输出后不用逗号。
e.g. 输入：12  输出：13,17,19,23,29

这个代码注意：
(1) 需要对输入小数情况进行判断，获取超过该输入的最小整数（这里没用floor()函数）；
(2) 对输出格式进行判断，最后一个输出后不增加逗号（这里没用.join()方法）。'''

# 标答
def prime(m):
    for i in range(2,m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n_ = int(n)
n_ = n_+1 if n_ < n else n_
count = 5

while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=",")
        else:
            print(n_, end="")
        count -= 1
    n_ += 1

# 函数方法，耦合
def int_Number(num):
    if type(num) == float:
        return int(num) + 1
    else:
        return num


def is_prime(m):
    int_Number(m)
    for i in range(2, m):
        if m % i == 0:
            return False
    return True


n = eval(input("请输入数字N: "))
count = 1
while count < 6:
    if is_prime(n) is True:
        if count < 5:
            print(n, end=",")
        else:
            print(n, end="")
        count += 1
    n += 1