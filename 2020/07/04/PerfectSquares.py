'''
279. Perfect Squares - Medium
https://leetcode.com/problems/perfect-squares/

Given a positive integer n, find the least number of 
perfect square numbers (for example, 1, 4, 9, 16, ...) 
which sum to n.

Examples:
	Input: n = 12
	Output: 3 
	Explanation: 12 = 4 + 4 + 4.

	Input: n = 13
	Output: 2
	Explanation: 13 = 4 + 9.

'''
import math
import numpy as np

def numSquares(n: int) -> int:

	def maths(n):
		if n <= 0: return 0 # takes care of 0 and negative numbers
		if (int(n**0.5)**2 == n): return 1 # takes care of perfect squares
		old_n = n
		'''
		Based on Lagrange's Four Square Theorem: 
		maximum of 4 perfect squares to sum to any number

		The result is 4 iff n can be written in the form:
		4^k(8*m + 7). Reference: Legendre's three-square theorem
		'''
		while n % 4 == 0:
			n /= 4
		if n % 8 == 7:
			return 4

		#n = old_n
		sqrt_n = int(n**0.5)
		print('sqrt_int({})={}'.format(n, sqrt_n))
		i = 0
		while i <= sqrt_n:
			if int((n-i**2)**0.5)**2 == n-i**2:
				return 2
			i += 1

		return 3

	def bfs_sol(n):
		if n <= 0: return 0
		base = math.floor(n ** 0.5) + 1
		# [1, 2, 3, ...] -> [1, 4, 9, ...]
		r = list(map(lambda x: x**2, list(range(base))[1:])) 
		
		if n == r[::-1][0]: # check to see if n is already a perfect square
			return 1

		check = {n}
		cnt = 0
		while check:
			print('cnt<{}> : {}'.format(cnt, check))
			cnt += 1
			temp = set()
			for x in check:
				for sq in r:
					if x == sq:
						return cnt
					if x < sq:
						break
					temp.add(x-sq)
					print('temp: {}'.format(temp))
			check = temp
			#print('   cnt<{}> : {}'.format(cnt, check))
		return cnt

	
	# dynamic programming answer from discussion
	def dp_sol(n):
		if n <= 0: return 0 # takes care of 0 and negative numbers
		if (int(n**0.5)**2 == n): return 1 # takes care of perfect squares
		INT_MAX = 2**64 - 1
		psq = [(INT_MAX) for p in range(n+1)]
		psq[0] = 0

		for i in range(1, n+1, 1):
			j = 1
			print('for i={}'.format(i))
			while j**2 <= i:
				print('  {}. MIN<{},{}>'.format(j, psq[i] if psq[i] != INT_MAX else 'INT_MAX', psq[i - j**2] + 1))
				psq[i] = min(psq[i], psq[i - j**2] + 1)
				j += 1



		return psq[::-1][0]

	return maths(n)

print(numSquares(7))
print(numSquares(12))
print(numSquares(13))
print(numSquares(64))
print(numSquares(36))