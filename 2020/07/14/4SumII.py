'''
454. 4Sum II - Medium
https://leetcode.com/problems/4sum-ii/

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 
2^31 - 1.

Example:

	Input:
	A = [ 1, 2]
	B = [-2,-1]
	C = [-1, 2]
	D = [ 0, 2]

	Output:
	2

	Explanation:
	The two tuples are:
	1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
	2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
def fourSumCount(A, B, C, D) -> int:
	A.sort(); B.sort(); C.sort(); D.sort(); # 4 * O(n)
	htable = {}
	res = 0
	for a in A: # O(n)
		for b in B: # O(n)
			if a + b in htable:
				htable[a+b] += 1
			else:
				htable[a+b] = 1
	for c in C: # O(n)
		for d in D: # O(n)
			if -(c + d) in htable:
				res += htable[-(c + d)]
	return res # 4 * O(n) + 2 * O(n^2) -> O(n^2)



A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

print('ANS->{}'.format(fourSumCount(A,B,C,D)))