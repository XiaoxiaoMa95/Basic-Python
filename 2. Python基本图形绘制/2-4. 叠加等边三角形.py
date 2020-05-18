'''叠加等边三角形的绘制'''

import turtle

turtle.setup(600, 600)
turtle.penup()
turtle.fd(-200)
turtle.seth(60)
turtle.pendown()

for i in range(3):
    turtle.fd(300)
    turtle.right(120)

turtle.penup()
turtle.fd(150)
turtle.seth(0)
turtle.pendown()

for i in range(3):
    turtle.fd(150)
    turtle.right(120)

turtle.done()
