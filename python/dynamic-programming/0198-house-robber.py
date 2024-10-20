'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
'''

from typing import List

def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    maxRobbed = [None for _ in range(n + 1)]

    maxRobbed[n] = 0
    maxRobbed[n - 1] = nums[-1]
    
    for i in range(n - 2, -1, -1):
        maxRobbed[i] = max(maxRobbed[i + 1], maxRobbed[i + 2] + nums[i])

    return maxRobbed[0]


nums1 = [1,2,3,1]
nums2 = [2,7,9,3,1]

print(rob(nums1))
print(rob(nums2))