'''
380. Insert Delete GetRandom O(1) - Medium
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom(): Returns a random element from current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
'''
from random import randint
from collections import OrderedDict

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = OrderedDict()
        self.LEN = 0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        try:
        	G = self.data[val]
        except KeyError as ke:
        	self.data[val] = val
        	self.LEN += 1
        	return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        try:
        	G = self.data[val]
        except KeyError as ke:
        	return False
        del self.data[val]
        self.LEN -= 1
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return list(self.data)[randint(0, self.LEN-1)]


obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(2))
print(obj.remove(3))
print(obj.insert(3))
print(obj.remove(4))
print(obj.remove(3))
print(obj.getRandom())

