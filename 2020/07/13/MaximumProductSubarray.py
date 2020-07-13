'''
152. Maximum Product Subarray - Medium
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
	Input: [2,3,-2,4]
	Output: 6
	Explanation: [2,3] has the largest product 6.

Example 2:
	Input: [-2,0,-1]
	Output: 0
	Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

def maxp(A) -> int:
	'''
	res = [float('inf')] * len(nums)
	neg = []
	i = 1
	res[i-1] = nums[i-1]
	while i < len(nums):
		if res[i-1] <= 0:
			res[i] = nums[i]
			neg.append(i-1)
		else:
			res[i] = res[i-1] * nums[i]
		i += 1

	print(res)
	print(neg)

	return 
	'''
	B = A[::-1] # O(n)
	# print(A)
	# print(B)
	for i in range(1, len(A)): # O(n-1)
		A[i] *= A[i-1] or 1
		B[i] *= B[i-1] or 1

	# print(A)
	# print(B)
	# print(A+B)
	return max(A+B)


print(maxp( [2,3,-2,4] ))
print(maxp( [-2,0,-1] ))
print(maxp( [2,3,-4,3,10,2,-1,8,8] )) # 64 * 24 * 60 i.e. all
print(maxp( [2,3,-4,3,10,2,0,8,8] )) # 64 i.e. 8 * 8
print(maxp( [-1,-3,5,2,3,-4,3,10,2,0,8,8,0,500] )) # 64 i.e. 8 * 8
print(maxp( [-2,3,1,5,-4,3,2,-1,9] ))
