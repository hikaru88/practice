#2
new_movies = []

recommend = input("オススメの映画は?:")
new_movies.append(recommend)


with open("rmovie.txt", "a", encoding="utf-8") as f:
    f.writelines(recommend+"\n")

print(new_movies)


"""
テキストファイル、rmovie.txtに、recommendの質問で入力された値を書き込みたい。
現在の問題点として、一つ一つの要素を改行して追加の書き込みをすることができない。

recommendに入力された値を、一度リストに格納してから、ファイルに移すことで可能となるかと考えたができなかった。
"""


#extra
new2_movies = []

recommend2 = input("オススメの映画は?:")
new2_movies.append(recommend2)

with open("rmovie.txt", "a") as f:
    for ele in new2_movies:
        f.write(ele+"\n")

"""
extraのコードによって、やっとできた。
まず、空のリストに、recommend2に入力された値を格納する。
次に、for文を使い、格納された値を行で書き出す。
これでできた
"""

"""
一番上のコードでもできた。
9行目を
f.writelines("\n".join(recommend))
から
f.writelines(recommend+"\n")
にすることでできるようになった。
"""
