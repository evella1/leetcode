# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells.
#  The same cell may not be used more than once in a word.


from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    path = set()

    def dfs(r, c, l):

        if len(word) == l:
                return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[l] or (r, c) in path:
            return False
        path.add((r, c))
        p = l + 1 #next letter in word
        res = (dfs(r + 1, c, p) or dfs(r, c + 1, p) or dfs(r - 1, c, p) or dfs(r, c - 1, p))
        path.remove((r, c))
        return res
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False    


board = [["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]]
word = "CAT"

print(exist(board, word)) # True

board = [["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]]

word = "BAT"

print(exist(board, word)) # False