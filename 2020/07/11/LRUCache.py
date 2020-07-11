'''
146. LRU Cache - Medium
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists 
in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently 
used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up: Could you do both operations in O(1) time complexity?

Example:

	LRUCache cache = new LRUCache( 2 /* capacity */ );

	cache.put(1, 1);
	cache.put(2, 2);
	cache.get(1);       // returns 1
	cache.put(3, 3);    // evicts key 2
	cache.get(2);       // returns -1 (not found)
	cache.put(4, 4);    // evicts key 1
	cache.get(1);       // returns -1 (not found)
	cache.get(3);       // returns 3
	cache.get(4);       // returns 4
'''

class LRUCache:
	'''
	i = 0
	pop = 0 # current population of keys
	cap = 0 # max pop of keys
	stack = deque([])
	data = {} # hash table

	def __init__(self, capacity: int):
		self.cap = capacity

	def get(self, key: int) -> int:
		# print('op:get')
		# print('pop={}, cap={}\nstack={}\ndata:\n'.format(self.pop,self.cap,self.stack,self.data))
		datum = self.data.get(hash(key))
		return [-1, datum][datum != None]

	def put(self, key: int, value: int) -> None:
		# print('op:put')
		# print('pop={}, cap={}\nstack={}\ndata:\n'.format(self.pop,self.cap,self.stack,self.data))
		if self.pop == self.cap:
			inv = None
			if self.i % 2 == 1:
				inv = self.stack.popleft() # 
			else:
				inv = self.stack.pop() # 
			self.data.pop(inv)
			self.pop -= 1
			self.i += 1
		self.data[hash(key)] = value
		self.stack.append((hash(key))) # appendleft())
		self.pop += 1

	def hash(key: int) -> int:
		return key % cap
	'''

	def __init__(self, MSize):
		self.size = MSize
		self.cache = {}
		self.next, self.before = {}, {}
		self.head, self.tail = '#', '$'
		self.connect(self.head, self.tail)

	def connect(self, a, b):
		self.next[a], self.before[b] = b, a

	def delete(self, key):
		self.connect(self.before[key], self.next[key])
		del self.before[key], self.next[key], self.cache[key]

	def append(self, k, v):
		self.cache[k] = v
		self.connect(self.before[self.tail], k)
		self.connect(k, self.tail)
		if len(self.cache) > self.size:
			self.delete(self.next[self.head])

	def get(self, key):
		if key not in self.cache: return -1
		val = self.cache[key]
		self.delete(key)
		self.append(key, val)
		return val

	def put(self, key, value):
		if key in self.cache: self.delete(key)
		self.append(key, value)

def test(cmds, vals):
	c = None

	for i in range(len(cmds)):
		if cmds[i] == "LRUCache":
			c = LRUCache(vals[i][0])
			print(None)
		elif cmds[i] == "get":
			print(c.get(vals[i][0]))
		else:
			key, val = vals[i]
			print(c.put(key, val))

	print('</>')

test(["LRUCache","get","put","get","put","put","get","get"],
	 [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
	)
