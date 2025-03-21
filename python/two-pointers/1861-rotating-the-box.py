# 1861. Rotating the Box

# You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.

from typing import List

def rotateTheBox(boxGrid: List[List[str]]) -> List[List[str]]:

    ROWS, COLS = len(boxGrid), len(boxGrid[0])

    for row in boxGrid:
        i = COLS - 1
        for c in range(COLS - 1, -1, -1):
            if row[c] == "#":
                row[c], row[i] = row[i], row[c]
                i -= 1
            elif row[c] == "*":
                i = c - 1

    result = []

    for c in range(COLS):
        arr = []
        for r in range(ROWS):
            arr.append(boxGrid[r][c])
        arr.reverse()
        result.append(arr)

    return result


print(rotateTheBox([["#",".","#"]]))
print(rotateTheBox([["#",".","*","."],["#","#","*","."]]))
boxGrid = [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]
print(rotateTheBox(boxGrid))