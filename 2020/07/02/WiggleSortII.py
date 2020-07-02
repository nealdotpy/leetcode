'''
324. Wiggle Sort II - Medium
https://leetcode.com/problems/wiggle-sort-ii/

Given an unsorted array nums, reorder it such that"
nums[0] < nums[1] > nums[2] < nums[3]....

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''

def wiggleSort(nums) -> None:
	# nums.sort()
	# for i in range(0, len(nums)-1, 1):
	# 	offset = 1
	# 	left = nums[i]
	# 	right = nums[i+offset]
	# 	while right == left and i+offset < len(nums)-1:
	# 		offset += 1
	# 		right = nums[i+offset]
	# 	print('Using offset: {} (i={}) and {}<->{}'.format(offset, i, left, right))
	# 	#left, right = right, left
	# 	nums[i] = right
	# 	nums[i+offset] = left
	# 	print(nums)
	# print('\n')
	nums.sort()
	half = len(nums[::2])
	nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
	print(nums)
	# https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof


wiggleSort([1, 5, 1, 1, 6, 4])
wiggleSort([1, 3, 2, 2, 3, 1])
wiggleSort([4,5,5,6])