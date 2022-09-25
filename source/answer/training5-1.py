import sys
import re

def f(string: str):
    return _rexp.sub(_replace, string)

_rexp = re.compile(r'\{(\w+)\}')


def _replace(match_data: re.sub):
    key = match_data.group(1)
    frame = sys._getframe(2)
    try:
        # ローカル変数の検索
        if key in frame.f_locals:
            return str(frame.f_locals[key])
        # グローバル変数の検索
        if key in frame.f_globals:
            return str(frame.f_globals[key])
        # なければ置き換えない
        return "{%s}" % key
    finally:
        # スタックフレームへの参照を消す
        # ローカル変数がスタックフレームを参照するため削除して循環参照を回避
        # またガーベージコレクションの負荷軽減
        del frame

w = 2000
h = 1000
print(f("width={w}, height={h}"))

'''
Point!
呼び出し元のスタックフレームにアクセスするための_getframe()は以下のドキュメントを参照してください。
* https://docs.python.org/ja/3/library/sys.html#sys._getframe
* https://www.curict.com/item/bd/bda1d29.html
'''