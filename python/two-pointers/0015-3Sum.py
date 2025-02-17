# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
# and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. 
# You may return the output and the triplets in any order.

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    
    result = []
    nums.sort()

    for ind, num in enumerate(nums):
        if ind > 0 and num == nums[ind - 1]:
            continue

        l, r = ind + 1, len(nums) - 1
        while l < r:
            threeSum = num + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                result.append([num, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums)) # [[-1,-1,2],[-1,0,1]]

nums = [0, 1, 1]
print(threeSum(nums)) # []