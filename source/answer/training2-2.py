# メタクラスを使用する
class HelloMeta(type):
    def __lshift__(self, value):
        print(f"Hello, {value}")

class Hello(object, metaclass=HelloMeta):
    pass


print("まずは想定通りの動作になっているか確認: ")
Hello << 'world'

print("----------------------------------")

print("演算子としてもちゃんと機能するか確認する: ")
Hello.__lshift__("world")
