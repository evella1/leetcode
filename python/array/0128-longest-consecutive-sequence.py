# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    max_seq = 0

    for num in nums_set:
        if num-1 not in nums_set:
            length = 1
            while num + length in nums_set:
                length += 1                    
            max_seq = max(max_seq, length)
    return max_seq

nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums)) # 4

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums)) # 9

nums = [1,2,0,1]
print(longestConsecutive(nums)) # 3

 