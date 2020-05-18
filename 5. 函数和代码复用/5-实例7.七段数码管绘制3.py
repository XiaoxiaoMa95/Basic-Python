'''步骤三：获得当前系统时间，绘制对应的数码管
1.增加七段数码管之间的线条间隔
2. 使用time库获取系统时间
3. 增加年月日标记 XXXx年XX月XX日
4.年月日标记与数字颜色不同'''

import turtle, time


def drawGap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)


def drawLine(draw):  # 绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)


def drawDigit(digit):  # 根据数字绘制七段数码管
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()  # 为后续数字确定位置
    turtle.fd(20)  # 为绘制后续数字确定位置


def drawDate(data):  # data为日期，格式为‘%Y-%m=%d+ e.g.2018-10=10+’ -年 =月 +日
    turtle.pencolor("red")
    for i in data:
        if i == '-':
            turtle.write('年', font=("Arial", 18, "normal"))  # 字体，字号
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle()
    turtle.done()


main()
