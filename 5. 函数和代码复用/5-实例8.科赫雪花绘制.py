'''进阶：N阶科赫雪花绘制
(1) 基本思路:
     -递归思想：函数 +分支
     -递归链条：线段的组合
     -递归基例：初始线段
(2) 分形几何是一种迭代的图，广泛存在于自然界中，请尝试选择一个新曲线绘制:
     -康托尔集、谢宾斯基三角形门格海绵 …
     -龙形曲线 、空间填充科赫…
     -函数递归的深入应用 …'''

import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main(level):
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.speed(0.5)
    for i in range(3):
        koch(400, level)
        turtle.right(120)
    turtle.hideturtle()
    turtle.done()


try:
    level = eval(input("请输入科赫曲线的阶: "))
    main(level)
except:
    print("输入错误")
