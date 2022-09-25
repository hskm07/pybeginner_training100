# for in ~ elseの使い方をしる
# else以下のコードは、for文が正常に実行できた時に実行される
# break文が実行されてしまうと、else文は実行されない。
# 先ほどと同様に数字と文字が混在したデータがあるとします。
numlist = [8,9,9,10,11,10,12,9,8]

# 文字が混在しているか、どれが文字かも分からないが、
# とりあえず全て数字だったら、作業時間の合計を出したい。
total = 0
for num in numlist :
    if not isinstance(num, (int, float)) :
        print(num, "数字でない値が含まれていました。")
        break
    # 数字だった時は合計値を計算
    total += num
else :
    # breakされなかったときは合計した値を出力する
    print("合計値：", total)

# 次に変数numlistの”10”のダブルクォーてションを外して実行しましょう。
# else以下が実行されるのを確認してください。
