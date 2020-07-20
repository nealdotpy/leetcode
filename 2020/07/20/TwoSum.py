'''
1. Two Sum - Easy
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
'''
from collections import OrderedDict
def twoSum(nums, target):
	'''
	arg: nums -> List[int] : list of numbers
	arg: target -> int : target to sum
	rtype: List[int]
	'''

	two_sum_hash_table = OrderedDict()
	return_indicies = []

	for index, number in enumerate(nums):
		# if target - number == number: # 6 - 3 = 3
		# 	if number in two_sum_hash_table:					
		# 		two_sum_hash_table[number + 0.1] = target - number
		# 	else:
		# 		two_sum_hash_table[number] = target - number + 0.1
		# else:
		# 	two_sum_hash_table[number] = target - number
		if number in two_sum_hash_table:
			two_sum_hash_table[number] = [two_sum_hash_table[number]] + [index]
		else:
			two_sum_hash_table[number] = index

	# for i, item in enumerate(two_sum_hash_table):
		# print('{}->{}-TARGET={} {}'.format(i,item,target-item,'NY'[target-item in two_sum_hash_table]))
	print(two_sum_hash_table)

	for i, key in enumerate(two_sum_hash_table):
		#print('dict={}, key={}, key in dict={}'.format(two_sum_hash_table,two_sum_hash_table[required_to_sum_to_target], two_sum_hash_table[two_sum_hash_table[required_to_sum_to_target]]))
		if target - key in two_sum_hash_table:
			if target - key == key and isinstance(two_sum_hash_table[key], list):
				return two_sum_hash_table[key]
			elif target - key != key:
				return_indicies.append(two_sum_hash_table[key])
				if len(return_indicies) > 1:
					return return_indicies

	#if target > 100: print(nums[28], nums[44], nums[45])
	return return_indicies

A = [0,4,3,0]
B = [3,2,4]
print(twoSum(A, 0))
print(twoSum(B, 6))
