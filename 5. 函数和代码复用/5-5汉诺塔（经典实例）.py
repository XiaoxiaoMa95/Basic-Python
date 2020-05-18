'''把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。
并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。
三根柱子A B C，起始都在Asrc柱上，n个圆盘,Cdst目的柱子，Bmid中间柱子
递归设计 只关心n和n-1个圆盘之间的关系'''

count = 0


def hanoi(n, src, mid, dst):  # hanoi(圆盘数量，起始柱子，中间过渡柱子，目的柱子)
    global count  # 全局变量，局部变量运行完会被清零
    if n == 1:  # 递归基例：只有一个圆盘，直接从起始柱子到目的主子
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:  # 递归链条 n个圆盘中，上n-1个圆盘从A-B，最后一个从A到C，再将B柱n-1个圆盘移到C柱子
        hanoi(n - 1, src, dst, mid)  # 将n-1个圆盘从A，到C，到B
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n - 1, mid, src, dst)  # 将n-1个圆盘从B，到A，到C


hanoi(3, "A", "B", "C")
print(count)
