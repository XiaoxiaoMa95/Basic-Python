'''format()方法的格式控制 {<参数序号>:<格式控制标记>
格式控制标记，格式内容如下：
: <填充> <对齐> <宽度> <,> <.精度> <类型>}'''

s = "PYTHON"
print("{0:30}".format(s))  # 默认左对齐
print("{0:>30}".format(s))  # 右对齐
print("{0:*^30}".format(s))  # 居中，使用*填充
print("{0:-^30}".format(s))  # 居中，使用-填充

# 逗号(,)用于显示千分位分隔符
print("{0:-^20,}".format(1234567890))
print("{0:-^20}".format(1234567890))   # 对比输出
print("{0:-^20,}".format(12345.67890))

# <.精度> 表示两个含义，由小数点(.)开头。对于浮点数，精度表示小数部分的有效输出位数。
# 对于字符串，精度表示输出的最大长度。
print("{0:.2f}".format(12345.67890))
print("{0:H^20.3f}".format(12345.67890))
print("{0:.4}".format("PYTHON"))

# <类型>表示输出整数和浮点数类型的格式规则。
# 整数输出：b-二进制；c-整数对应的Unicode字符；d-十进制；o-八进制；x-小写十六进制；X-大写十六进制
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))
# 浮点数输出：e-小写字母e的指数形式；E-大写字母E的指数形式；f-浮点数的标准浮点形式；%-浮点数的百分形式
print("{0:e},{0:E},{0:f},{0:%}".format(3.14))
print("{0:.2e},{0:.2E},{0:.2f},{0:.2%}".format(3.14))

