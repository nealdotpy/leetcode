'''
179. Largest Number - Medium
https://leetcode.com/problems/largest-number/

Given a list of non negative integers, arrange 
them such that they form the largest number.

Examples:
	Input: [10,2]
	Output: "210"

	Input: [3,30,34,5,9]
	Output: "9534330"
'''

def largest_number(nums) -> str:
	if not any(nums):
		return '0'
	ans = sorted(map(str, nums), key=functools.cmp_to_key(lambda a1, a2: -1 if a1+a2>a2+a1 else (1 if a1+a2<a2+a1 else 0)))
	return ''.join(ans)

print(largest_number([10,2]))
print(largest_number([3,30,34,5,9]))
print(largest_number([3,321,398,32,30,34,5,9,351,]))
