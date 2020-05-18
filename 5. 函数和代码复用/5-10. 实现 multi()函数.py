'''实现multi()函数，参数个数不限，返回所有参数的成积'''


def multi(x):
    s = list(x.split(","))  # 输入一串数字，以逗号分割
    sum = 1
    count = 1
    for item in s:
        if type(eval(item)) == int or type(eval(item)) == float:
            sum *= eval(item)
        else:
            print('第{}项不是一个有效数字！'.format(count))
        count += 1
    return sum


a = input("请输入一串数字，以逗号分割: ")
print(multi(a))
