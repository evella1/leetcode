
def lengthOfLongestSubstring(s: str) -> int:

    seen = set()
    max_len, l = 0, 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        max_len = max(max_len, r - l + 1)

    return max_len


print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))