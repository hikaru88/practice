#1
movie = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

for movies in movie:
    print(movies)


#2
for count in range(25, 51):
    print(count)


#3
i = 0
for shows in movie:
    print(i)
    print(movie[i])
    i += 1
    if i == 4:
        break


#4
collect = [3, 38, 59, 79]

while True:
    a = input("数字を入力してください:")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("数字を入力するか、qで終了します。")
    if a in collect:
        print("正解")
    else:
        print("不正解")


#5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for x in list1:
    for j in list2:
        list3.append(x * j)

print(list3)
