'''从键盘输入一行字符，编写程序，统计并输出其中的英文字符、数字、空格和其他字符的个数'''

str = input("请输入一行字符")
number_of_character = 0
number_of_num = 0
number_of_tab = 0
number_of_other = 0
for c in str:
    if ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z"):
        number_of_character += 1
    elif ord("0") <= ord(c) <= ord("9"):
        number_of_num += 1
    elif c == " ":
        number_of_tab += 1
    else:
        number_of_other += 1
print("英文字符{}个，数字{}个，空格{}个，其他字符{}个".format( \
    number_of_character, number_of_num, number_of_tab, number_of_other))
