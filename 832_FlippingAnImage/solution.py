from typing import List

def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    invert = lambda x: 0 if x==1 else 1
    return [list(map(invert, item)) for item in [row[::-1] for row in A]]


A = [[1,1,0],[1,0,1],[0,0,0]]
print(A)
print(flipAndInvertImage(1, A))

B = [[1,1,0,0],[1,0,0,1],[0,1,1,1]]
print(len(B))
print(len(B[0]))
print(B)
print(flipAndInvertImage(1, B))
