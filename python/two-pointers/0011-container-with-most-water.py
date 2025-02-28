# 11. Container With Most Water

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from typing import List

def maxArea(heights: List[int]) -> int:
    l, r = 0, len(heights) - 1
    result = 0

    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        result = max(result, area)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return result


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # 49

height = [1,1]
print(maxArea(height))  # 1