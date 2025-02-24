# # 853. Car Fleet


# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

# You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

# A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

# Return the number of car fleets that will arrive at the destination.



from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed)) # 3

target = 10
position = [6,8]
speed = [3,2]
print(carFleet(target, position, speed)) # 2

target = 10
position = [0,4,2]
speed = [2,1,3]
print(carFleet(target, position, speed)) # 1