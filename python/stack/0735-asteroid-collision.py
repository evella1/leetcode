from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    i = 0
    while i < len(asteroids):
        asteroid = asteroids[i]
        if stack and (asteroid < 0 and stack[-1] > 0):
            if abs(asteroid) == abs(stack[-1]):
                stack.pop()
            elif abs(asteroid) > abs(stack[-1]):
                stack.pop()
                continue  # Re-evaluate the current asteroid
            # else do nothing if the stack's top asteroid is larger
        else:
            stack.append(asteroid)
        i += 1
    
    return stack


print(asteroidCollision([5,10,-5]))
print(asteroidCollision([8,-8]))
print(asteroidCollision([10,2,-5]))