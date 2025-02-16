# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == '1':
                        queue.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands
    
# Time complexity: O(m*n)
# Space complexity: O(m*n)

#Tests
s = Solution()
assert s.numIslands([
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]) == 1
assert s.numIslands([
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]) == 4
assert s.numIslands([]) == 0
assert s.numIslands([["1"]]) == 1
assert s.numIslands([["0"]]) == 0
assert s.numIslands([["1", "0"]]) == 1
assert s.numIslands([["1", "1"]]) == 1
assert s.numIslands([["1"], ["1"]]) == 1
assert s.numIslands([["1"], ["0"]]) == 1
assert s.numIslands([["1", "0"], ["0", "1"]]) == 2
assert s.numIslands([["1", "1"], ["1", "1"]]) == 1
assert s.numIslands([["1", "1"], ["1", "0"]]) == 1
assert s.numIslands([["1", "1"], ["0", "0"]]) == 1
assert s.numIslands([["1", "0"], ["0", "0"]]) == 1
assert s.numIslands([["0", "0"], ["0", "0"]]) == 0
assert s.numIslands([["0", "1"], ["0", "0"]]) == 1
assert s.numIslands([["0", "1"], ["1", "0"]]) == 2
assert s.numIslands([["1", "1"], ["0", "1"]]) == 1
assert s.numIslands([["1", "0"], ["1", "1"]]) == 1
assert s.numIslands([["1", "0"], ["1", "0"]]) == 1