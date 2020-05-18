import turtle

turtle.setup(500,500)
turtle.pensize(5)

for i in range(4):
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.fd(100)
    turtle.penup()
    turtle.fd(50)
    turtle.right(90)

turtle.done()
