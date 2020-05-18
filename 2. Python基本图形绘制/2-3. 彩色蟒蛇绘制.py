'''改造实例2的代码。绘制一条彩色蟒蛇，即在绘制蟒蛇的每个小段时，画笔的绘制颜色会发生变化
提示：将画笔颜色控制函数放在蟒蛇绘制函数附近'''

import turtle


def drawSnake(radius, angle):
    turtle.circle(radius, angle)
    turtle.circle(-radius, angle)


def drawNeck(radius, angle, neck):
    turtle.circle(radius, angle / 2)
    turtle.fd(radius)
    turtle.circle(neck, 180)
    turtle.fd(radius * 2 / 3)


turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)
turtle.pencolor("yellow")
drawSnake(40, 80)
turtle.pencolor("black")
drawSnake(40, 80)
turtle.pencolor("pink")
drawSnake(40, 80)
turtle.pencolor("blue")
drawSnake(40, 80)
turtle.pencolor("red")
drawNeck(40, 80, 16)
turtle.done()
