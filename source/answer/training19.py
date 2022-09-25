# リストに要素を追加する：append()関数
# appendは要素を追加するためのリストの機能
# append()はリストの後ろに追加されていく
data = [100,99,40,29,30,31]
data.append(6)
print(data)
data.append(50)
print(data)

# リストに要素を追加する：insert()関数
# insert()関数は、挿入位置を指定して値を挿入することができます。
number_list = ['one', 'two', 'three', 'four', 'five']
number_list.insert(0,"zero")
print(number_list)
number_list.insert(6,"six")

# リストから要素を取り除くpop()関数
# 最後に追加した値から順にデータを取り出す。（LIFO：Last　In　First　Outといいます。）
fruits = ["apple", "orange", "banana", "peach"]
dessert = fruits.pop()
print(dessert, ':', fruits)
dessert = fruits.pop()
print(dessert, ':', fruits)
