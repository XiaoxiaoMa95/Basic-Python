'''基本统计值：给出一组数据，对他们有个概要理解
表示为组合数据类型，数据总个数、求和、平均值、方差、中位数
总个数：len()
求和：for...in逐个遍历，求和
平均值：求和/总个数
方差：各数据与平均数差的平方的和的平均数
中位数：排序，然后 奇数个找中间，偶数个找中间2个取平均值
'''


def getNum():
    # 获取用户不定长度输入。获得用户的每一个数据输入，知道用户输入空为止；
    # 不确定数量的用户输入，使用保留字while
    nums = []
    iNumStr = input("请输入数字(回车退出): ")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出): ")
    return nums


def mean(numbers):  # 计算平均值
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)


def dev(numbers, mean):  # 计算方差
    sdev = 0.0
    for num in numbers:
        sdev += (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


def median(numbers):  # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med


n = getNum()
m = mean(n)
print("平均值:{},方差:{:.2},中位数:{}".format(m, dev(n, m), median(n)))
