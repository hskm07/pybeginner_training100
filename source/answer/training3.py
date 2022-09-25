# 文字列の連結
moziA = "I have "
moziB = "a "
moziC = "pen."
print(moziA + moziB + moziC)

'''
Point! 文字列の連結

  '文字列' + '文字列'

解説: 文字列は「+」を使うと結合してます。2個でも3個でも結合できます。
'''

# 数値と文字列の連結
price = 1000
unit = "yen"
print(str(price) + unit)

'''
Point! 文字列と数値の結合の注意点

  '文字列' + str(数値)

解説：文字列と数値は結合できません。理由はデータ型の不一致です。
結合するには、str()関数で数値を文字列に変換する必要があります。

'''

