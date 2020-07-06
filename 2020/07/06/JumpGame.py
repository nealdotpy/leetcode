'''
55. Jump Game - Medium
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially 
positioned at the first index of the array.

Each element in the array represents your maximum jump 
length at that position.

Determine if you are able to reach the last index.

Example 1:
	Input: nums = [2,3,1,1,4]
	Output: true
	Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
	Input: nums = [3,2,1,0,4]
	Output: false
	Explanation: You will always arrive at index 3 no matter what. 
	Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
	1 <= nums.length <= 3 * 10^4
	0 <= nums[i][j] <= 10^5
'''

def canJump(nums) -> bool:
	'''
	if len(nums) <= 1: return True
	target = len(nums) - 1 # last index 
	pos = 0 # current position
	old_pos = 0
	while pos < target+1:
		#old_pos = pos
		print('[old_pos={}] @pos={}; nums[pos]={}'.format(old_pos, pos, nums[pos]))
		if pos == target:
			return True
		elif nums[pos] == 0 and nums[old_pos] == 0:
			return False
		elif nums[pos] == 0 and nums[old_pos] != 0:
			#pos = old_pos
			nums[old_pos] = nums[old_pos] - 1 if nums[old_pos] > 0 else 0
			pos = old_pos
		else:
			#print('pos: {}; new-pos: {}'.format(pos, pos+nums[pos]))
			old_pos = pos
			pos += nums[pos]
			#nums[pos] = nums[pos] - 1 if nums[pos] > 0 else 0
	return True
	'''
	target = len(nums) - 1
	for i in range(len(nums)-2, -1, -1):
		print('i+nums[i]>=target --> {}+{}>={}'.format(i, nums[i], target))
		if i + nums[i] >= target:
			target = i
	return target == 0


print(canJump([2,3,1,1,4])) # true
print(canJump([3,2,1,0,4])) # false
print(canJump([3,3,1,0,4])) # true
print(canJump([2,0])) # true
print(canJump([0])) # true
print(canJump([1,1,2,2,0,1,1])) # true
