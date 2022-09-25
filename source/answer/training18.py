# 使用する変数
number_list = [1,9,2,8,10]
mozi_list = ["apple", "orange", "Grape", "Pear", "Melons"]
place_list = ["青森", "和歌山", "山梨", "千葉", "茨城"]

# 多重リストの作成
multi_list = [number_list, mozi_list, place_list]
# 多重リストの表示
print(multi_list)

# 構造的にわかりにくいと思います。
# 要素参照しながらデータの構造を確認
# multi_listから1を取り出したい
print(multi_list[0][0])
# multi_listからappleを取り出したい
print(multi_list[1][0])
# multi_listから青森を取り出したい
print(multi_list[2][0])
# multi_listから9を取り出したい
print(multi_list[0][1])
# multi_listから2を取り出したい
print(multi_list[0][2])
# # multi_listからPearを取り出したい
print(multi_list[1][3])
# multi_listから千葉を取り出したい
print(multi_list[2][3])
# multi_listから茨城を取り出したい
print(multi_list[2][4])

# 多重リストの値を変更する
# 8 を　99に変更
multi_list[0][3] = 99
# 和歌山を近畿に変更
multi_list[2][1] = "近畿"
# 結果を表示
print(multi_list)