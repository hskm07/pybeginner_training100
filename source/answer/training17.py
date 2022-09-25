# リスト内のデータを表示する。
colors = ["red", "blue", "yellow", "white", "black"]
# リストcolorsの１番目の値を取得
print(colors[0])
# リストcolorsの２番目の値を取得
print(colors[1])
#  リストcolorsの５番目の値を取得
print(colors[4])
#　リストcolorsの最後の値を取得
print(colors[-1])
# len()関数を使ってリストの要素の数を調べる（データの長さを調べるといいます。）
print(len(colors))
# 最初の値"red"を"green"に変える
colors[1] = "green"
# 最後の"black"を orangeに変える
colors[2] = "orange"
# リストを確認
print(colors)


# for文を使ってリストの要素を取り出す
# list値の長さを取得してfor文に活用すると便利
number = [100,23,4,593,0.4,38,449,201,29,384,2,1,0]
print(f"リストnumberの長さ{len(number)}")
for num in number:
    print(f"リストnumberの値は{num}")