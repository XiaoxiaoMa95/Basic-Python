'''月球上物体的体重是在地球上的16.5%，假如你在地球一年增长0.5kg。
编写程序计算出未来十年你在地球和月球上的体重状况'''

Weight = eval(input("请输入你的体重(Kg): "))
Weight_On_Earth = Weight + 0.5 * 10
Weight_On_Moon = Weight_On_Earth * 0.165
print("十年后你在地球上的体重是：{0:.2f},在月球上的体重是{1:.2f}". \
      format(Weight_On_Earth, Weight_On_Moon))
