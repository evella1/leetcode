# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False] * n
    for i in range(n):
        for word in wordDict:
            if i < len(word) - 1:
                continue
            if (i == len(word) - 1) or (dp[i - len(word)]):
                if s[i - len(word) + 1: i + 1] == word:
                    dp[i] = True
                    break
    return dp[-1]


print(wordBreak("leetcode",["leet","code"]))
print(wordBreak("applepenapple",["apple","pen"]))
print(wordBreak("catsandog", wordDict = ["cats","dog","sand","and","cat"]))