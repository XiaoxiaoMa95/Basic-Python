'''工作日的努力
工作日模式要努力到什么程度，才能与每天努力1%相同呢
A君：一年365天，每天进步1%，不停歇
B君：一年365天，每周做五休二，休息日下降1%，工作日要多努力呢？

def...while...("笨办法"试错)'''


def dayUp(df):  # def保留字定义一个函数，其中df=dayfactor 根据df参数计算工作日力量，参数不同，代码可共用
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup


dayfactor = 0.01
while dayUp(dayfactor) < 37.78:  # while保留字判断条件是否成立，调用dayUp函数，条件成立时循环执行
    dayfactor += 0.001
print("工作日的努力参数是:{:.3f}".format(dayfactor))
