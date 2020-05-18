'''利用turtle库绘制一个正方形螺旋线'''

import turtle

turtle.pensize(2)
turtle.seth(90)
length=5
for i in range (21):
    turtle.fd(length)
    turtle.left(90)
    turtle.fd(length)
    turtle.left(90)
    length+=5
turtle.fd(length)
turtle.done()
