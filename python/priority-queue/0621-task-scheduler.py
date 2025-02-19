# Link: https://leetcode.com/problems/task-scheduler/
# 621. Task Scheduler

# You are given an array of CPU tasks, each labeled with a letter from A to Z,
# and a number n. Each CPU interval can be idle or allow the completion of one task.
# Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.


from collections import deque
import heapq
from typing import Counter, List


def leastInterval(tasks: List[str], n: int) -> int:
    time = 0
    
    dct = Counter(tasks)
    heap = [-x for x in dct.values()]
    
    heapq.heapify(heap)
    queue = deque()

    while queue or heap:
        time += 1
        if heap:
            cnt = 1 + heapq.heappop(heap)
            if cnt:
                queue.append([cnt, time + n])
        if queue and queue[0][1] == time:
            heapq.heappush(heap, queue.popleft()[0])

    return time
    

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval(tasks, n))  # Output: 8

tasks = ["A","C","A","B","D","B"]
n = 1
print(leastInterval(tasks, n))  # Output: 6

tasks = ["A","A","A","B","B","B"]
n = 3
print(leastInterval(tasks, n))  # Output: 10
