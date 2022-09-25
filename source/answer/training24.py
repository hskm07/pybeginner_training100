list_parents = [10,20,30,40,50]

# list_parentsを複製する
list_child = list_parents
# ここでlist_childの先頭の値に99を代入する
list_child[0] = 99
# 両方のリストを確認する
print("list_parents: ",list_parents)
print("list_child: ",list_child)

print("-------------------------")

# 正しくリストを複製する
# list_parentsを複製する
list_child = list_parents.copy()
# ここでlist_childの先頭の値に99を代入する
list_child[0] = 99

# 両方のリストを確認する
print("list_parents: ",list_parents)
print("list_child: ",list_child)