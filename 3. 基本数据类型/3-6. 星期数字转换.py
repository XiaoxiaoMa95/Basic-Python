'''WeekNamePrint
程序读入一个表示星期几的数字（1~7），输出对应的星期字符串名称
输入数字，输出对应的星期'''

# Solution1
weekStr= "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入星期数字:"))
pos=(weekId-1)*3
print(weekStr[pos:pos+3])

#Solution2
weekStr="一二三四五六七"
weekId = eval(input("请输入星期数字："))
print("星期"+weekStr[weekId-1])