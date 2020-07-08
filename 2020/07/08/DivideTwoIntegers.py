'''
29. Divide Two Integers - Medium
https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor, divide two integers 
without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means 
losing its fractional part. 

For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:
	Input: dividend = 10, divisor = 3
	Output: 3
	Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
	Input: dividend = 7, divisor = -3
	Output: -2
	Explanation: 7/-3 = truncate(-2.33333..) = -2.

Note:
	* Both dividend and divisor will be 32-bit signed integers.
	* The divisor will never be 0.
	* Assume we are dealing with an environment which could only store 
	integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
	For the purpose of this problem, assume that your function 
	returns 231 − 1 when the division result overflows.
'''
def divide(top: int, bottom: int) -> int:
	''' NAIVE: O(n)
	quo = 0 # quotient
	rem = 0 # remainder
	MIN, MAX = -2**31, 2**31-1
	neg = (top>=0) ^ (bottom>=0)
	top, bottom = abs(top), abs(bottom)
	if bottom == 1: 
		quo = top
	else:
		for i in range(top, 0, -bottom):
			if i - bottom >= 0:
				quo += 1
			else: 
				rem = i
	quo = (-1 if neg else 1) * quo
	if quo > MAX:
		quo = MAX
	elif quo <= MIN:
		quo = MIN

	return quo
	'''

	# BETTER: O(log)
	neg = (top>=0) ^ (bottom>=0)
	top, bottom = abs(top), abs(bottom)
	res = 0
	while top >= bottom:
		temp, i = bottom, 1
		while top >= temp:
			print('top={}, temp={}, res={}, i={}'.format(top, temp, res, i))
			top -= temp
			res += i
			i <<= 1 # *2
			temp <<= 1 # *2
	res = -res if neg else res
	return min(max(-2**31, res), 2**31-1)



print(divide(10, 3))
print(divide(-10, 3))
print(divide(10, -3))
print(divide(-10, -3))
print(divide(7, -3))
print(divide(-2147483648, -1))
print(divide(-2147483648, 1))
print(divide(2147483648, 1))
print(divide(2147483648, 2))