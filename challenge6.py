#1
a = "カミュ"
print(a[0])
print(a[1])
print(a[2])



#2
content = input("何を書きましたか？:")
place = input("どこに送りましたか？:")
print("私は昨日{}を書いて、{}に送った！".format(content, place))



#3
sentence = "aldous Huxley was born in 1894."
print(sentence.title())



#4
x = "どこで? 誰が? いつ?".split(" ")
print(x)



#5
y = ["The", "fox", "jumped", "over", "the", "fence","."]
y = " ".join(y)
y = y[0:-2] + "."
print(y)



#6
z = "A screaming comes across the sky."
z = z.replace("s", "$")
print(z)



#7
v = "Hemingway"
print(v.index("m"))



#8
print("それはある晴れた\"昼下がり\"の出来事だった。")

"""
バックスラッシュ(\)の打ち方
optionキーを押しながら¥キーを押すことでできる。
"""



#9
f = "three" + " three" + " three"
print(f)

kakezan = " three"
kakezan = kakezan * 3
kakezan = kakezan[1:]
print(kakezan)



#10
sentence2 = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
sentence2 = sentence2[0:10]
print(sentence2)
