#アプローチとしては、
#* 各段数はリストを作成しデータを格納
#* 最後に各要素をjoinする 
#1段目：[" ", "1", " ", " ",...]
# 2段目：["0", " ", "2", " ",...]
# 3段目：[" ", " ", " ", "3",...]


from typing import List # このモジュールはなくても構いません。

def snake_character(chars: str) -> List[List[str]]:
    result = [[],[],[]] # 
    result_indexes = {0,1,2}
    insert_index = 1 # どの段数からスタートするかを示すインデックス
    for i ,s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(' ')
    return result
numbers=[str(i) for j in range(5) for i in range(10)]
strings = ''.join(numbers)
for line in snake_character(strings):
    print(''.join(line))
# 参考：[リストの内包表記](https://docs.python.org/ja/3/tutorial/datastructures.html#list-comprehensions)