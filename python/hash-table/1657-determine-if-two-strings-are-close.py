# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, 
# and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

from typing import Counter

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    count1, count2 = Counter(word1), Counter(word2)

    if count1.keys() != count2.keys() or sorted(count1.values()) != sorted(count2.values()):
        return False

    return True


print(closeStrings("abc", "bca"))
print(closeStrings("a", "aa"))
print(closeStrings("cabbba", "abbccc"))


      