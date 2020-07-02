'''
18. 4Sum - Medium
https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.
'''

def three_sum(nums, value):
	print('passed in: {}::{}'.format(nums, value))
	nums.sort() # [-,0,+]
	ans = []
	length = len(nums)

	for i in range(length-1):
		#if nums[i] > 0: break
		if i>0 and nums[i] == nums[i-1]: continue

		l, r = i+1, length-1

		while l < r:
			total = nums[i] + nums[l] + nums[r]

			if total > -value:
				r -= 1
			elif total < -value:
				l += 1
			else:
				ans.append([nums[i], nums[l], nums[r]])
				while l < r and nums[l] == nums[l+1]:
					l += 1
				while l < r and nums[r] == nums[r-1]:
					r -= 1
				l += 1
				r -= 1


	return ans

def four_sum(nums, target):
	ans = []
	nums.sort()
	length = len(nums)

	for i in range (length-1):
		if i>0 and nums[i] == nums[i-1]: continue
		tout = nums[i] - target
		res = three_sum(nums[i+1:], tout)
		for trpl in res:
			trpl.append(tout+target)
			trpl.sort()
			ans.append(trpl)
		print(ans)


	return ans

#print(four_sum([1, 0, -1, 0, -2, 2], 0))
print(four_sum([-1,-5,-5,-3,2,5,0,4], -7))