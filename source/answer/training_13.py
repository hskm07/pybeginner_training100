# if文の基礎
# ランダムに数字を発生させるrandomを使用するために必要な一文
import random

rd = random.randint(1,100)
print("ランダムで発生させた数字は{0}です。".format(rd))

# if文の開始は、必ずインデントをつける
if rd >= 50:
    #インデントの開始でif文開始（行の始めから半角空白4つあける）
    print("合格！")
#インデントの終了：if文の終了


'''
Point!
ランダムな数字の発生は、randomモジュールを使用します。
参考：https://docs.python.org/ja/3/library/random.html
今は、
1. 一行目に「import random」を記述して
2. 「random.randint(数字１,数字２)」を使うと、
3. 数字１〜数字２の間でランダムな数字を作ることができるという認識程度で構いません。

モジュールのインポートがわからない人は、以下のURLを確認してください
https://note.nkmk.me/python-import-usage/
'''
