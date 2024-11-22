
# Given an m x n matrix, return all elements of the matrix in spiral order.

from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    right, bottom, left, top = len(matrix[0]) - 1, len(matrix) - 1, 0, 0

    while top <= bottom and left <= right:

        #right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        #down
        for j in range(top, bottom + 1):
            result.append(matrix[j][right])
        right -= 1

        #left
        if top <= bottom:
            for k in range(right, left - 1, -1):
                result.append(matrix[bottom][k])
        bottom -= 1

        #up
        if left <= right:
            for m in range(bottom, top - 1, -1):
                result.append(matrix[m][left])
        left += 1

        
    return result

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))