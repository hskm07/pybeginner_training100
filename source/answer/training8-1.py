#数字の比較
num1 = 100
num2 = 100
num3 = 200

jdg1 = (num1 == num2)
jdg2 = (num1 == num3)
print("評価結果:jdg1:", jdg1, "評価結果:jdg2:", jdg2)
print("比較結果: ", jdg1 and jdg2)

jdg1 = (num1 == num2)
jdg2 = (num1 != num3)
print("評価結果:jdg1:", jdg1, "評価結果:jdg2:", jdg2)
print("比較結果: ", jdg1 and jdg2)

jdg1 = (num1 >= num2)
jdg2 = (num1 == num3)
print("評価結果:jdg1:", jdg1, "評価結果:jdg2:", jdg2)
print("比較結果: ", jdg1 or jdg2)

# 文字の比較
msg = "今日は朝ごはんを食べましたか"
ans = "No"

if ans == "Yes":
    print("比較結果: ", "素晴らしい")
else:
    print("比較結果: ", "残念")



# 論理値とは、真/偽 ON/OFF YES/NO TRUE/FALSEという２択のこと
""" 比較する時に使用する演算子：比較演算子
    ==  a == b     aとbが等しい時にTrue
    !=  a != b     aとb等しくない時にTrue
    >   a >  b     aがbより大きいときTrue
    >=  a >= b     aがb以上の時にTrue
    <   a <  b     aがbより小さい時にTrue
    <=  a <= b     aがb以下の時にTrue
"""
