# 微实例1：try-except
try:
    num=eval(input("请输入一个整数："))
    print(num**2)
except NameError:
    print("输入错误，请输入一个整数！")

# 微实例2：try-except-else-finally
try:
    alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx=eval(input("请输入一个整数: "))
    print(alp[idx])
except NameError:
    print("输入错误，请输入一个整数！")
else:
    print("没有发生异常")
finally:
    print("程序执行完毕，不知是否发生了异常")
