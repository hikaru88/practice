#1
love_music = ["米津玄師", "miwa", "sumica"]

print(love_music[2])


#2
熱海 = ("35.109713", "139.052206")
箱根 = ("35.190711", "139.026019")
トロント = ("43.6532", "-79.3831")

prace_detail = []

prace_detail.append(熱海)
prace_detail.append(箱根)
prace_detail.append(トロント)

print(prace_detail)


#3
mycharastic = {"好きな色":"灰色", "好きな食べ物":"パスタ", "好きな映画":"グレイテスト・ショーマン", "好きなアーティスト":"米津玄師", "趣味":"料理"}


#4
n = input("知りたいことを入力してください:")
if n in mycharastic:
    print(mycharastic[n])
else:
    print("その情報はまだありません")


#5
like_artist = {"米津玄師":"春雷", "miwa":"ハツナツ", "radwimps":"ふたりごと", "ずっと真夜中でいいのに":"秒針を噛む"}
