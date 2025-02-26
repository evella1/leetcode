# 705. Design HashSet

# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class ListNode:

    def __init__(self, value):
        self.val = value
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hashSet = [ListNode(-1) for x in range(10**3)]

    def add(self, key: int) -> None:
        index = key % 10**3
        cur = self.hashSet[index]
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % 10**3
        cur = self.hashSet[index]
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % 10**3
        cur = self.hashSet[index]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

obj = MyHashSet()
obj.add(1)  # set = [1]
obj.add(2)  # set = [1, 2]  
print(obj.contains(1)) # return True
print(obj.contains(3)) # return False
obj.add(2) # set = [1, 2]
print(obj.contains(2)) # return True
obj.remove(2) # set = [1]
print(obj.contains(2)) # return False
