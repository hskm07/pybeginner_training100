import json
import os

from pathlib import Path

class JSONSyntaxError(SyntaxError):
    pass

# 読み込むjosnファイルの定義
json_path = Path("source", "input", "sample.json")
try:
    with open(json_path, mode="r", encoding="utf-8") as fjson:
        json_data = json.load(fjson)
except json.decoder.JSONDecodeError as ex:
    ## JSONのエラーのトレースバックは表示しない
    libpath = os.path.dirname(json.__file__)
    tb = ex.__traceback__
    while tb.tb_next is not None:
        pyfile = tb.tb_next.tb_frame.f_code.co_filename
        if pyfile.startswith(libpath):
            tb.tb_next = tb.tb_next.tb_next
        else:
            tb = tb.tb_next
    # JSONのエラー箇所を表示する
    err_message = ex.args[0]
    lineno = ex.lineno
    column = ex.colno
    with open(json_path) as f:
        line = f.readlines()[lineno-1]
    new_excpt = JSONSyntaxError(err_message, (json_path, lineno, column, line))
    new_excpt.__traceback__ = ex.__traceback__
    # 例外を再送する
    raise new_excpt from None