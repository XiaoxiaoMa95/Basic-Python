'''采用3-9的模型。
以7天为周期，连续学习3天能力值不变，从第4天开始至第7天每天能力值增长为前一天的1%。
如果7天中有1天间断学习，则周期从头计算。
如果初始能力值为1，固定每10天休息一天，365天后的能力值是多少？
如果每15天休息1天呢？'''

# 每10天休息一天
dayUp=1.0
dayfactor=0.01
for i in range(1,366):
    if i % 11 in [4,5,6,7]:
        dayUp=dayUp*(1+dayfactor)
print("the result is {:.3f}". format(dayUp))

# 每15天休息一天
dayUp=1.0
dayfactor=0.01
for i in range(1,366):
    if i%16 in [4,5,6,7,11,12,13,14]:
        dayUp = dayUp * (1 + dayfactor)
print("{}the result is {:.3f}".format(dayfactor,dayUp))
