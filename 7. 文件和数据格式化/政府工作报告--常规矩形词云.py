'''需求：对于政府工作报告等政策文件，如何直观理解
体会直观的价值：生成词云&优化词云                政府工作报告等文件 --> 有效的词云展示

基本思路：1.读取文件、分词整理；2、设置并输出词云；3.观察结果，优化迭代'''

import jieba
import wordcloud

f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()

ls = jieba.lcut(t)  # 将文本分词，分词结果保存为列表类型
txt = " ".join(ls)  # 用空格将列表的元素连接，形成由空格分隔的长字符串

w = wordcloud.WordCloud( \
    width=1000, height=700, \
    background_color="white", font_path="msyh.ttc")  # 生成词云对象
w.generate(txt)
w.to_file("grwordcloud.png")
