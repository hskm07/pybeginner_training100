from typing import List

def generate_pascal_triangle(depth: int) -> List[List[int]]:
    data = [
        [1] * (i + 1) for  i in range(depth)
    ]
    for line in range(2, depth):
        for i in range(1, line):
            data[line][i] = data[line-1][i-1] +  data[line-1][i]
    return data
    
if __name__ == "__main__":
    print(generate_pascal_triangle(4))