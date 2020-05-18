import jieba
import wordcloud


from imageio import imread#读取图片文件，并将其变为图片文件表达的内部变量
mask = imread ("chinamap.jpg")

excludes = {}
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()

ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud( \
    width=1000, height=700, \
    background_color="white", font_path="msyh.ttc", mask=mask)
w.generate(txt)
w.to_file("grwordcloud2.png")
