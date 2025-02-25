# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:

    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for j in range(len(nums) - 1, -1, -1):
        result[j] *= postfix
        postfix *= nums[j]

    return result

nums = [1,2,3,4]
print(productExceptSelf(nums)) # [24,12,8,6]

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums)) # [0,0,9,0,0]