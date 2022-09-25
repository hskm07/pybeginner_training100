# for文のネストとリスト
# 例えば、Excelからこんな名前データが抜き出せました。
# 名前データに、ランダムに5回生成した数字の合計値を結びつけ出力します。
# ライブラリ宣言
import random
# 変数宣言
name = ["内田", "安里", "小島", "森田", "鈴木", "明神"]

# ループには文字列でもOK
# この時最後のprint関数は、どのfor文に関わると思いますか。
for i in name :
    point = 0
    for j in range(5):
        point += random.randint(0,100)

    print("{0}さんは、ポイント{1}点です。".format(i, point))
