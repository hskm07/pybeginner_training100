# for文の基礎:コードを記述
print("0~9まで繰り返し実行")
for i in range(10):
    # インデントの開始 = for文の開始
    print(i)
# インデントの終了 = for文の終了

# range()関数に慣れる
# range(開始値,終了値,ステップ)
# ステップはいくつずつ増加させるか。通常は＋1ずつされる。
print("3~8まで繰り返し実行")
for i in range(3,9):
    print(i)

print("1~10まで3つずつ増加し値を出力")
for i in range(1,10,3):
    print(i)

print("5~9まで１つずつ増加し値を出力")
for i in range(5,10):
    print(i)
