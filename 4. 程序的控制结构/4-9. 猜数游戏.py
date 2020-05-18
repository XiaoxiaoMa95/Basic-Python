'''在程序中预设一个0~9之间的整数，让用户通过键盘输入所猜的数。
如果大于预设的数，显示“遗憾，太大了”；小于预设的数，显示“遗憾，太小了”，
如此循环，知道猜中该数，显示“猜测N次，你猜中了！”，其中N是用户输入数字的次数'''

import random

num = random.randint(0, 9)
tim = 0
while True:   # 或者写作 while 1:
    number = eval(input("请输入一个0~9之间的整数: "))
    tim+=1
    if number < num:
        print("遗憾，太小了")
    elif number >num:
        print("遗憾，太大了")
    else:
        print("猜测{}次，你猜中了！".format(tim))
        break
