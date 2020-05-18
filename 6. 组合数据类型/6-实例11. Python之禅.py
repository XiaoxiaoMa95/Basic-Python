# 字符串s，该字符串非明文，将字符串转化为明文
s = """Gur Mra bs Clguba, ol Gvz Crgref
Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl
gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er
Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq
vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs
gubfr!"""

# 将字符串转化为明文
d = {}   # 定义空字典d
for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)
        # 对字典d填充了内容，将i+c对应的字符替换为(i + 13) % 26 + c，即将编号循环增加了13。
        # chr(65)代表字符'A', chr(97)代表字符'a'，
        # 循环建立了字母a到z和字母A到Z的一个13位循环移动对应表
print("".join([d.get(c, c) for c in s]))
