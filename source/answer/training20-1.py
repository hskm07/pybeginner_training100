num = [1,2,3,4,5,6,7,8,9,10]
num_double = [n if n % 2 == 0 else n*2 for n in num]
print(num_double)

num = [1,2,3,4,5]

tmp = []
for i in num:
    tmp.append(i*2)
num[:] = tmp
print(num)