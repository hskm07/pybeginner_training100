age = 10
is_adult = "大人です" if age >= 20 else "未成年です"
print(is_adult)

age = 40
is_adult = "大人です" if age >= 20 else "未成年です"
print(is_adult)

'''
最初のコードをif文で表すと、、、
if age >= 20:
    is_adult = "大人です"
else:
    is_adult = "未成年です"

if文で条件分岐させて、変数に値を代入するコードは長ったらしいですが、
三項演算子で表現することで、スッキリコードが書けるし、
Pythonとしてはこっちの方がベストプラクティスとされている。
'''