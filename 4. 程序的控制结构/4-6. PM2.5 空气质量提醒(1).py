'''PM2.5指的是大气中直径小于或等于2.5μm的可吸入颗粒物
计算机通过PM2.5指数分级发布空气质量提醒。简化版的空气质量标准采用三级模式。
输入：接收外部输入的PM2.5值
处理：大于75，打印空气污染警告；35~75，打印空气质量良，建议适度户外活动；
     小于35，打印空气质量优，建议户外活动
输出：打印空气质量提醒'''

PM=eval(input("请输入PM2.5数值: "))
if 0<=PM<35:
    print("空气质量优，建议户外活动！")
elif 35<=PM<=75:
    print("空气质量良，建议适度户外活动！")
else:
    print("空气污染！")
