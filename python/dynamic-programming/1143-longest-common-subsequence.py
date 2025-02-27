# 1143. Longest Common Subsequence

# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


def longestCommonSubsequence(text1: str, text2: str) -> int:
    dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # for line in dp:
    #     print(line)

    return dp[-1][-1]


text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))  # 3

text1 = "abc"
text2 = "def"
print(longestCommonSubsequence(text1, text2))  # 0

text1 = "abc"
text2 = "abc"
print(longestCommonSubsequence(text1, text2))  # 3

