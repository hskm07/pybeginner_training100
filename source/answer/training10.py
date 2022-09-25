# 簡単計算クイズ
# 入力はキーボードから入力を受け付けるinput関数を使用する
# 入力を３回間違える、もしくはキーボードの「q」が入力されたら、break
from random import randint
# 変数のセット
miss = 0
correct = 0
print("問題：次の計算結果を入力してください。3回間違えたら終了")

while miss < 3:
    # ランダムで数値を生成する
    a = randint(1,100)
    b = randint(1,200)
    ans = a + b
    # 問題の表示
    question = f"{a} + {b}は？"
    # input()でキーボードからの入力を待つ
    value = input(question)
    # もしキーボードの「q」が押されたら、while文をbreakで終了
    if value == "q" :
        break
    # 入力された結果が正解かどうか判定する。
    if value == str(ans) :
         correct += 1
         print("正解です。")
    else :
        miss += 1
        print("間違いです。間違えた回数：{0}".format(miss))

print("-" * 20)
print("正解回数：", correct)
print("間違い回数：", miss)
