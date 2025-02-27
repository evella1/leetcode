# 62. Unique Paths

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 10**9.

 
def uniquePaths(m: int, n: int) -> int:
    dp = [[0 for _ in range(n + 1)] for j in range(m + 1)]
    
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if i == 1 and j == 1:
                dp[i][j] = 1
            else: 
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]   

    return dp[-1][-1]

    #Alternative approach with a single row DP reducing space complexity of O(n)
    # dp = [1] * n  # Single row DP array
    # print(dp)
    # for i in range(1, m):  # Start from the second row
    #     for j in range(1, n):  # Start from the second column
    #         dp[j] += dp[j - 1]  # Update current cell by adding left cell

    # return dp[-1]

m = 3
n = 7
print(uniquePaths(m, n)) #28

n = 2
print(uniquePaths(m, n)) #3