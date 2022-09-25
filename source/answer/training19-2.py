# [1,3,3,5,5,7,7,7,10,12,12,15] => [1,3,5,7,10,12,15]

from typing import List

def delete_duplicate_verison1(numbers: List[int]) -> None:
    tmp = []
    for num in numbers:
        if num not in tmp:
            tmp.append(num)
    numbers[:] = tmp
    

def delete_duplicate_verison2(numbers: List[int]) -> None:
    tmp = [numbers[0]]
    i, len_num = 0, len(numbers) -1
    while i < len_num:
        if numbers[i] != numbers[i+1]:
            tmp.append(numbers[i+1])
        i += 1
    numbers[:] = tmp
    

def delete_duplicate_verison3(numbers: List[int]) -> None:
    i = len(numbers) -1
    while i > 0:
        if numbers[i] == numbers[i-1]:
            numbers.pop(i)
        i -= 1
        


if __name__ == "__main__":
    pre = [1,3,3,5,5,7,7,7,10,12,12,15] 
    delete_duplicate_verison1(pre)
    print(pre)
    
    pre = [1,3,3,5,5,7,7,7,10,12,12,15] 
    delete_duplicate_verison2(pre)
    print(pre)
    
    pre = [1,3,3,5,5,7,7,7,10,12,12,15] 
    delete_duplicate_verison3(pre)
    print(pre)