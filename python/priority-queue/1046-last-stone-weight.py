
# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

from typing import List
import heapq


def lastStoneWeight(stones: List[int]) -> int:
    
    if len(stones) == 1:
        return stones[0]

    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)
        if x > y:
            heapq.heappush(stones, y - x)
        
    return -stones[0] if stones else 0


# Time complexity: O(nlogn)

stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))  # 1

stones = [2,2]
print(lastStoneWeight(stones))  # 0