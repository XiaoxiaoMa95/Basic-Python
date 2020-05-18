'''改编4-10程序，当用户输入不是整数(如字母、浮点数等)时，程序会终止自动退出。
改编该程序，当用户输入出错时给出“输入内容必须为整数!"的提示，并让用户重新输入'''

import random

num = random.randint(0, 100)
tim = 0
while True:
    number = eval(input("请输入您猜测的数字: "))
    if int(number) == number:
        tim += 1
        if number < num:
            print("遗憾，太小了")
        elif number > num:
            print("遗憾，太大了")
        else:
            print("猜测{}次，你猜中了！".format(tim))
            break
    else:
        print("输入内容必须为整数!")
