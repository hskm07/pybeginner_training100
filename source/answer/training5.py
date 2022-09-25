# format()の練習
msg = "私の年齢は{0}歳で、出身地は{1}です。趣味は{2}です。".format(29,"東京都","釣り")
print(msg)

# f-stringの練習
lineno = "300"
filename = "sample.py"
print(f"このコードはエラーです。ファイル:{filename}[行番号{lineno}]")

'''python
f-stringやフォーマット文字列は、エラーメッセージのカスタマイズや
デバッグメッセージのカスタマイズでよく利用されます。
便利なので、利用できるようにしておきましょう。
'''
