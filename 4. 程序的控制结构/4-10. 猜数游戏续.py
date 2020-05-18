'''改编4-9，让计算机能随机产生一个预设数字，范围在0~100之间，其他游戏规则不变'''

import random

num = random.randint(0, 100)
tim = 0
while True:   # 或者写作 while 1:
    number = eval(input("请输入您猜测的数字: "))
    tim+=1
    if number < num:
        print("遗憾，太小了")
    elif number >num:
        print("遗憾，太大了")
    else:
        print("猜测{}次，你猜中了！".format(tim))
        break
