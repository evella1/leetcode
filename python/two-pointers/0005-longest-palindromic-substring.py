#5. Longest Palindromic Substring

# Given a string s, return the longest substring of s that is a palindrome.

# A palindrome is a string that reads the same forward and backward.

# If there are multiple palindromic substrings that have the same length, return any one of them.


def longestPalindrome(s: str) -> str:
    def helper(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]  # Correct slicing

    result = ""
    
    for i in range(len(s)):
        # odd-length palindromes
        odd_palindrome = helper(i, i)
        if len(odd_palindrome) > len(result):
            result = odd_palindrome

        # even-length palindromes
        even_palindrome = helper(i, i + 1)
        if len(even_palindrome) > len(result):
            result = even_palindrome

    return result


s = "babad"
print(longestPalindrome(s))  # Output: "bab" or "aba"

s = "cbbd"
print(longestPalindrome(s))  # Output: "bb"