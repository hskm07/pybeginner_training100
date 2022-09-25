# stationに"C":"千代田線"を追加してみましょう。
# 追加前
station = {
    "G": "銀座線", #随時コメントも入れていく
    "M": "丸ノ内線", # 途中で改行するときは、カンマのつけ忘れに注意
    "H": "日比谷線",
    "Z": "半蔵門線",
    "TX": "つくばエクスプレス" 
}
print(station)

# 追加後
station['C'] = "千代田線"
print(station)

# 辞書型のデータとリストを組み合わせてデータを作る
keys = ["鈴本", "加藤", "金", "朴", "金子"]
value = [30, 28, 32, 22, 33]
# zip関数：２つ以上のリストをまとめることができる
personal_data = dict(zip(keys, value))
# personal_dataを出力
print(personal_data)
# 要素の取り出し
print(personal_data['金子'])

# 辞書の値を更新する
# personal_dataの、鈴本さんのデータを変え、新たに２人の情報追加する
new_personal = {"鈴本":40, "本田":20, "小渕":21}
personal_data.update(new_personal)
print(personal_data)
