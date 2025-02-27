
# 424. Longest Repeating Character Replacement


# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


def characterReplacement(s: str, k: int) -> int:

    l = 0
    hashMap = {}
    result = 0
    
    for r in range(len(s)):
        hashMap[s[r]] = 1 + hashMap.get(s[r], 0)

        while ((r - l + 1) - max(hashMap.values())) > k:
            hashMap[s[l]] -= 1
            l += 1
        result = max(result, r - l + 1)

    return result

s = "ABAB"
print(characterReplacement(s, 2))  # 4

s = "AABABBA"
print(characterReplacement(s, 1))  # 4

s = "A"
print(characterReplacement(s, 0))  # 1