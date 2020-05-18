'''用函数简化代码，输出一个更大的田字格'''


def drawSqure(n):
    line = 3 * n + 1
    for i in range(1, line + 1):
        if i % 3 == 1:
            print("+----" * n, end="")
            print("+")
        else:
            print("|    " * n, end="")
            print("|")


def main():
    n = eval(input("请输入你要的阶数"))
    drawSqure(n)


main()
