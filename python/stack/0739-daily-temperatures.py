# 739. Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for curr_day, curr_temp in enumerate(temperatures):
        while stack and curr_temp > temperatures[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = curr_day - prev_day
        stack.append(curr_day)
    return answer

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))  # [1, 1, 4, 2, 1, 1, 0, 0]

temperatures = [30, 40, 50, 60]
print(dailyTemperatures(temperatures))  # [1, 1, 1, 0]

temperatures = [30, 60, 90]
print(dailyTemperatures(temperatures))  # [1, 1, 0]