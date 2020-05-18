'''参数为一个字符串，如果这个字符串属于整数、浮点数或复数的表示，则返回True，否则返回False

提示：python中合法的数字有十进制整数、十六进制整数、浮点数、复数
-----------3 也是合法数字'''


def isNum(num):
    try:
        np = '+-'
        if num[0] in np:
            # 字符串以 +— 开头
            return isNum(num[1:])
        elif type(eval(num)) == int or type(eval(num)) == float or \
                type(eval(num)) == complex:
            return True
    except:
        return False


# 测试集
print(isNum('Hello'))
print(isNum('+++++++++++++++++++++'))
print(isNum('+-+-+--3'))
print(isNum('100'))
print(isNum('10e10'))
print(isNum('10e+10'))
print(isNum('10e10.'))
print(isNum('10e10e'))
print(isNum('10e10+4E10'))
print(isNum('10e+1j'))
print(isNum('10e+1.j'))
print(isNum('1.0e+10-j'))
print(isNum('1.0e+1j-3.e'))
print(isNum('0abddf'))
print(isNum('0xabddf'))
