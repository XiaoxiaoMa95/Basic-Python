'''第二种引用函数库的方法：
from <库名> import <函数名，函数名，..., 函数名>
from <库名> import *     #其中 *是通配符，表示所有函数
此时，调用该函数库时不再使用库名，直接使用如下格式：
<函数名>(<函数参数>)'''

from turtle import *

setup(650, 350, 200, 200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("violet")
seth(-40)
for i in range(4):
    circle(40, 80)
    circle(-40, 80)
circle(40, 80 / 2)
fd(40)
circle(16, 180)
fd(40 * 2 / 3)
done()
