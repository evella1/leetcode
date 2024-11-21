# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
# so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.


def minRemoveToMakeValid(s: str) -> str:
    if not s:
        return ""

    stack = []
    result = []

    for ind, char in enumerate(s):
        if char == "(":
            stack.append((char, ind))
        elif char == ")":
            if stack and stack[-1][0] == "(":
                stack.pop()
            else:
                stack.append((char, ind))
    
    indices = [x[1] for x in stack]

    for ind, char in enumerate(s):
        if ind not in indices:
            result.append(char)

    return "".join(result)


print(minRemoveToMakeValid("lee(t(c)o)de)"))
print(minRemoveToMakeValid("a)b(c)d"))
print(minRemoveToMakeValid("))(("))
