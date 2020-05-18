'''实现isOdd（）函数，参数为整数，要有异常处理
如果整数是奇数，返回True，否则返回False'''


def isOdd(n):
    try:
        if type(n) == type(1):
            if n % 2 == 0:
                return False
            else:
                return True
        else:
            raise TypeError
    except TypeError:
        print("这不是一个有效的整数！")


print(isOdd(4))
print(isOdd(3))
print(isOdd(-1))
print(isOdd('str'))
print(isOdd(3.0))
