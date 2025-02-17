
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    
    result = []


    def dfs(i, current_arr, total):
        if total == target:
            result.append(current_arr.copy())
            return
        if i >= len(candidates) or total > target:
            return

        current_arr.append(candidates[i])
        dfs(i, current_arr, total + candidates[i])

        current_arr.pop()
        dfs(i + 1, current_arr, total)

    dfs(0, [], 0)
    return result



candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target)) # [[2,2,3],[7]]

candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target)) # [[2,2,2,2],[2,3,3],[3,5]]