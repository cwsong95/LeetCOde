# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the get and put operations.
# get(key) : Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) : Set or insert the value if the key is not already present.
# When the cache reached its capacity, put(key, value) should invalidate the least recently used item before inserting a new item.
# The cache is initialized with a positive capacity.

from collections import deque

class LRUCache:
  def __init__(self, capacity: int):
    self.c = capacity
    self.m = dict()
    self.deq = deque()

  def get(self, key: int) -> int:
    if key in self.m:
      value = self.m[key]
      self.deq.remove(key)
      self.deq.append(key)

      return value
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    if key not in self.m:
      # check if length of deque is in full capacity
      if len(self.deq) == self.c;
        # remove Least used item
        oldest = self.deq.popleft()
        del self.m[oldest]
    else:
      self.deq.remove(key)

    self.m[key] = value
    self.deq.append(key)