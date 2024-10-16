'''
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.
If there is no such integer in the array, return 0.
'''
import math
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            divisors = set()
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    if i != num // i:
                        divisors.add(num // i)
                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                result += sum(divisors)

        return result
    
sol = Solution()

nums1 = [21,4,7]
nums2 = [21,21]
nums3 = [1,2,3,4,5]

print(sol.sumFourDivisors(nums1))
print(sol.sumFourDivisors(nums2))
print(sol.sumFourDivisors(nums3))