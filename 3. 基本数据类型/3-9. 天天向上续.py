'''天天向上续。尽管每天坚持，人的能力发展不是无限的，它符合特定的模型。
假设能力增长符合如下带有平台期的模型：
以7天为周期，连续学习3天能力值不变，从第4天开始至第7天每天能力值增长为前一天的1%。
如果7天中有1天间断学习，则周期从头计算。
编程回答，如果初始能力值为1，连续学习365天后能力值是多少'''

dayfactor = 0.01
dayUp = 1.0

for i in range(366):
    if i % 7 in [1, 2, 3]:
        dayUp = dayUp
    else:
        dayUp = dayUp * (1 + dayfactor)
print("{:.3%} the result is {:.2f}".format(dayfactor, dayUp))
