'''实现isPrime()函数，参数为整数，要有异常处理。
如果整数是质数，返回True，否则返回False'''


def isPrime(n):
    try:
        if type(n) == float:
            raise TypeError
        elif n == 1:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
    except TypeError:
        print("这不是一个有效数字")


a = eval(input())
print(isPrime(a))
