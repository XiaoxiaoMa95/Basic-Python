'''描述
使用turtle库，绘制一个正方形。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬'''

import turtle
turtle.penup()
turtle.bk(100)
turtle.pendown()
turtle.width(3)
turtle.pencolor("blue")
for i in range(4):
    turtle.fd(100)
    turtle.left(90)
turtle.done()