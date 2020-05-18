import turtle  #调用turtle函数
turtle.setup(650,350,200,200)  #设置绘图窗体 宽650 高350 左上角坐标（200，200）
turtle.penup() #抬起画笔，海龟飞行
turtle.fd(-250) #向后直线250像素，不留下痕迹
turtle.pendown() #放下画笔，海龟爬行
turtle.pensize(25) #画笔宽度25像素
turtle.pencolor("purple")  #画笔颜色purple
turtle.seth(-40)  #海龟方向改为绝对角度-40度
for i in range(4):  #绘制4个循环，蟒蛇的4个身体关节
    turtle.circle(40,80)  #半径40像素，绘制80度弧度
    turtle.circle(-40,80)  #半径-40像素，绘制80度弧度
turtle.circle(40,80/2)  #半径40像素，绘制40度弧度，少半个弧形，脖子部分
turtle.fd(40)
turtle.circle(16,180)  #半圆形+直线，绘制头部
turtle.fd(40*2/3)
turtle.done()  #程序运行结束，不会自动退出，手工关闭窗体退出；若需自动退出，去掉最后一行代码