'''
155. Min Stack - Easy
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum 
element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack:

	def __init__(self):
		self.min_stack = []
		self.size = 0
		
	def push(self, x: int) -> None:
		if not self.min_stack:
			self.min_stack.append((x, x))
		else:
			self.min_stack.append((x, min(x, self.min_stack[self.size - 1][0])))
		self.size += 1

	def pop(self) -> None:
		self.min_stack.pop(self.size - 1)
		self.size -= 1

	def top(self) -> int:
		return self.min_stack[size - 1]

	def getMin(self) -> int:
		return self.min_stack[size - 1][1]