'''分形几何--科赫曲线（雪花曲线）   用Python绘制科赫曲线
科赫曲线是de Rham曲线的特例。
1.给定线段AB，科赫曲线可以由以下步骤生成： 2.将线段分成三等份（AC,CD,DB）
3.以CD为底，向外（内外随意）画一个等边三角形DMC  4.将线段CD移去   分别对AC,CM,MD,DB重复1~3。
递归链条：线段的组合
递归基例：初始线段'''

import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            # 在画笔前进方向的0，60，-120，60°分别绘制n-1阶科赫曲线
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.setup(800, 400)
    turtle.speed(0)  # 控制绘制速度，采用turtle.speed()
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600, 3)  # 0阶科赫曲线长度，阶数
    turtle.hideturtle()


main()
