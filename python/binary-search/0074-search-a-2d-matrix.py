# 74. Search a 2D Matrix

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    
    def findRow(matrix, target):
        rows = len(matrix)
        l, r = 0, rows - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return (mid, True)
            elif matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1

        return (-1, False)
    
    row, value = findRow(matrix, target)
    if value:
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
    else:
        return False

    return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target)) # True

target = 13
print(searchMatrix(matrix, target)) # False