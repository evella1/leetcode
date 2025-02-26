# 169. Majority Element

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Follow-up: Could you solve the problem in linear time and in O(1) space?



from typing import List

def majorityElement(nums: List[int]) -> int:
        # time O(n) space O(n)
        #    dct = Counter(nums)
        # return max(dct, key=lambda y: dct[y])

        # time O(n) space O(1)
        currMax, currMaxCount = 0, 0
        for n in nums:
            if currMaxCount == 0:
                currMax = n
                currMaxCount = 1
            elif n == currMax:
                currMaxCount += 1
            else:
                currMaxCount -= 1

        return currMax

nums = [3,2,3]
print(majorityElement(nums)) # 3

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums)) # 2

