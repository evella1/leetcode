'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
'''
from typing import List

def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
        
    return max(rob_helper(nums[:-1]), rob_helper(nums[1:]))

def rob_helper(nums: List[int]) -> int:
    n = len(nums)
    maxRobbed = [None for _ in range(n + 1)]

    maxRobbed[n] = 0
    maxRobbed[n - 1] = nums[-1]
        
    for i in range(n - 2, -1, -1):
        maxRobbed[i] = max(maxRobbed[i + 1], maxRobbed[i + 2] + nums[i])

    return maxRobbed[0]


nums1 = [2,3,2]
nums2 = [1,2,3,1]
nums3 = [1,2,3]

print(rob(nums1))
print(rob(nums2))
print(rob(nums3))