'''
50. Pow(x, n) - Medium
https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
	Input: 2.00000, 10
	Output: 1024.00000

Example 2:
	Input: 2.10000, 3
	Output: 9.26100

Example 3:
	Input: 2.00000, -2
	Output: 0.25000
	Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
	* -100.0 < x < 100.0
	* n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''

def _pow(x: float, n: int) -> float:
	'''
	neg = x < 0 # assigning negative at the end
	inv = n < 0 # inverting at the end -> 1/y
	if x == 1 or n == 0: return 1
	elif x == 0: return 0
	elif n == 1: return x
	elif n == -2^31: return 0
	'''
	if n < 0:
		x = 1 / x
		n = -n
	res = 1
	while n:
		if n & 1: # % 2; 0 -> even -> false, 1 -> odd -> true
			res *= x
		x *= x
		n >>= 1 # //= 2
	return res





print(_pow(2, 10)) # 1024.000000
print(_pow(2.1, 3)) # 9.26100
print(_pow(2, -2)) # 0.25