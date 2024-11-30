'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by
starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
'''
from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if not intervals:
        return [newInterval]

    # Insert the new interval
    index = 0

    for i in range(len(intervals)):
        if newInterval[0] <= intervals[i][0]:
            break
        index += 1

    intervals.insert(index, newInterval)

    # Merge intervals
    merged_array = [intervals[0]]
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if start <= merged_array[-1][1]:
            merged_array[-1][1] = max(merged_array[-1][1], end)
        else:
            merged_array.append(intervals[i])

    return merged_array


intervals1 = [[1,3],[6,9]]
newInterval1 = [2,5]

intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4, 8]

print(insert(intervals1, newInterval1))
print(insert(intervals2, newInterval2))