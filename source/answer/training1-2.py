# https://docs.python.org/ja/3/library/functions.html#type

# インスタンスメソッドの定義
def hello(self):
    print(f"Hello, {self.name}!")

dict_ = {
    "name": "world", # クラス変数
    "hello": hello # インスタンスメソッド
}

name = "Hello" # クラス名
baseobj = (object, ) #　親クラス

# クラスオブジェクト作成
Hello = type(name, baseobj, dict_)

# 生成結果を出力
print(Hello)
print(f"クラス変数{Hello.name}")

# インスタンスオブジェクトを作成できるか確認
Hello().hello()


class Name(object):
    def __init__(self):
        print("Hi")
        
print(type(Name))