'''
33. Search in Rotated Sorted Array - Medium
https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot 
unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return 
its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''
def search(nums, target) -> int:
	'''
	def find_pivot(nums) -> int:
		mid = len(nums) // 2
		left, right = 0, len(nums) - 1
		while left < right:
			if nums[mid] > nums[right] and nums[mid] > nums[left]: # pivot is more right
				left = mid
				mid = left + mid // 2
			elif nums[mid] < nums[right] and nums[mid] < nums[left]: # pivot is more left
				right = mid
				mid //= 2
			elif nums[mid] == nums[right] or nums[mid] == nums[left]: # found pivot
				return 

	'''
	left, right = 0, len(nums)
	while left < right:
		mid = (left + right) // 2
		if (nums[mid] < nums[0]) == (target < nums[0]):
			if nums[mid] < target:
				left = mid + 1
			elif nums[mid] > target:
				right = mid
			else:
				return mid
		elif target < nums[0]:
			left = mid + 1
		else:
			right = mid
	return -1
