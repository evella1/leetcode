# # 150. Evaluate Reverse Polish Notation

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


from typing import List



def evalRPN(tokens: List[str]) -> int:
    # Mapping operators to lambda functions.
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b)  # int() truncates towards zero.
    }
    stack = []
    for token in tokens:
        if token in ops:
            # Pop the last two numbers.
            b = stack.pop()
            a = stack.pop()
            # Apply the operator and push the result back.
            stack.append(ops[token](a, b))
        else:
            # If it's not an operator, convert it to an integer.
            stack.append(int(token))
    return stack[0]



# Time complexity: O(n)
# Space complexity: O(n)

# Let's test the function with the sample testcase
tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))  # 9

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))  # 6             

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens)) # 22