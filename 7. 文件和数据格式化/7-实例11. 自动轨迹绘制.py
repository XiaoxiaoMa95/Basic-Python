'''需求：根据脚本绘制图形，不是写代码而是写数据绘制轨迹
数据脚本是自动化最重要的第一步
基本思路：1.定义数据文件格式（接口）；2。编写程序，根据文件接口解析参数绘制图形；3.编制数据文件
e.g. 300，0，144，1，0，0
     300（行进距离），1（转向判断 0:左转，1：右转），144（绝对转向角度），0，1，0（RGB三个通道颜色，0-1的浮点数）'''

import turtle as t  # 将turtle别名为t

t.title('自动绘制轨迹')  # 设置绘图标题栏的信息
t.setup(800, 600, 0, 0)  # 设置绘图窗口大小
t.pencolor("red")
t.pensize(5)

# 数据读取，将所有信息读入后，保存为列表，遍历每行
datals = []  # 空列表
f = open("data.txt")  # 打开数据文件
for line in f:  # 遍历每一行
    line = line.replace("\n", "")  # 将文件每行结尾的换行符，转变为空字符串
    datals.append(list(map(eval, line.split(","))))
    # 对于每一行中6个数据，以字符串形式表示且以逗号分隔。.split（）以逗号作为分隔符，将字符串分割，形成一个列表，列表中每一个元素都是字符串形式
    # map(,)函数，对于组合数据类型中的每一个元素，都执行第一个参数所对应的函数。第一个参数eval，对应eval（）。列表中每一个元素变成数字
    # 将列表读入datals作为一个元素，datals中的元素又是一个列表[[],[]...[]]
f.close()

# 自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:  # if datals[i][1] != 0：
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
