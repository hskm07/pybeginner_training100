# タプルの基礎を学習する
# タプルもリストと同様、複数の値を一つの変数で扱うことができます。
# 書式はかっこで囲んで、カンマで区切るだけ。ただし、かっこはなくてもいい。
testA = ("book", "car", "color", 101, 99.9)
print(testA)

testB = ("py", 3.6)
print(testB)

# こんな感じでネストも可能
tp_nest = (testA, testB)
print(tp_nest)

# タプルの連結
testC = testA + testB
print(testC)

# tuple()を使ってタプルを作る
week_t = tuple("日月火水木金土")
print("week_t", week_t, " データ型：", type(week_t))
# タプルをリストに変換する
week_l = list(week_t)
print("week_l", week_l, "   データ型：", type(week_l))
