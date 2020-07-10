'''
91. Decode Ways - Medium
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers 
using the following mapping:
	'A' -> 1
	'B' -> 2
	...
	'Z' -> 26
Given a non-empty string containing only digits, determine the total 
number of ways to decode it.

Example 1:
	Input: "12"
	Output: 2
	Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:
	Input: "226"
	Output: 3
	Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

def num_decodings(s: str) -> int:

	''' close solution -> small bug
	def o(n: str) -> bool:
		return 10 < int(n) <= 26

	def d(n: str) -> int:
		if o(n):
			return 2
		return 1

	if int(s[0]) == 0: return 0
	if len(s) == 1: return 1
	if len(s) == 2 and not o(s): return 1

	res = [0] * len(s)
	res[0] = d(s[:2])
	omega = 1.0 if o(s[:2]) else 0.0
	print('i={}: {}, o={}'.format(s[:2], res, omega), end=' ')
	for i in range(2, len(s), 1):
		nxt = s[i-1:i+1]
		print(' next->{}'.format(nxt))
		res[i-1] = res[i-2] + [d(nxt) * omega, 0][o(nxt)]
		if o(nxt) and o(s[:i]):
			res[1] -= 1
			omega += 0.5
		elif o(nxt): 
			omega += 1
		print('i={}: {}, o={}'.format(s[:i+1], res, omega), end =' ')

	print()


	return int(res[len(s)-2])
	'''
	if not s:
		return 0

	dp = [0 for x in range(len(s) + 1)] 
	
	# base case initialization
	dp[0] = 1 
	dp[1] = 0 if s[0] == "0" else 1   #(1)

	for i in range(2, len(s) + 1): 
		# One step jump
		f = ''
		if 0 < int(s[i-1:i]) <= 9:    #(2)
			dp[i] += dp[i - 1]
			f += '+'
		# Two step jump
		if 10 <= int(s[i-2:i]) <= 26: #(3)
			dp[i] += dp[i - 2]
			f += '+'

		print('0 < {} <= 9 | 10 <= {} <= 26'.format(s[i-1:i],s[i-2:i]))
		print('n->{} dp: {}{}'.format(s[:i], dp, f))

	return dp[len(s)]


print(num_decodings('17251813')) # 14
print(num_decodings('12469135')) # 6
# print(num_decodings('12')) # 2
# print(num_decodings('226')) # 3
print(num_decodings('22613')) # 6
# print(num_decodings('1')) # 1
# print(num_decodings('0')) # 0
# print(num_decodings('10')) # 1
print(num_decodings('101')) # 1
# print(num_decodings('01')) # 0


