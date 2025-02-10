
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from typing import Counter, List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    
    freq_arr = [[] for i in range(len(nums) + 1)]
    for key, v in count.items():
        freq_arr[v].append(key)

    result = []
    for j in range(len(freq_arr) - 1, -1, -1):
        if freq_arr[j]:
            for element in freq_arr[j]:
                if len(result) == k:
                    return result
                result.append(element)
    
    return result

# Bucket sort
# Time complexity: O(n)
# Space complexity: O(n)

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))  # [1, 2]

nums = [1]
k = 1
print(topKFrequent(nums, k))  # [1]