# Given an integer array nums and an integer k,
# return the k most frequent elements.
# You may return the answer in any order.

from typing import Counter, List

def topKFrequent(nums: List[int], k: int) -> List[int]:

    count = Counter(nums)

    return [k for k, _ in count.most_common(k)]

nums1 = [1,1,1,2,2,3]
k1 = 2

nums2 = [1]
k2 = 1

print(topKFrequent(nums1, k1))
print(topKFrequent(nums2, k2))