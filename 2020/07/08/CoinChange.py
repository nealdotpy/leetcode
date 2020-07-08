'''
322. Coin Change - Medium
https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount 
of money amount. Write a function to compute the fewest number of 
coins that you need to make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return -1.

Example 1:
	Input: coins = [1, 2, 5], amount = 11
	Output: 3 
	Explanation: 11 = 5 + 5 + 1

Example 2:
	Input: coins = [2], amount = 3
	Output: -1

Note: You may assume that you have an infinite number of each kind of coin.
'''

def change(coins: list, amount: int) -> int:
	#coins = coins.sort()[::-1] # guarentees order, descending 
	MAX = float('inf')
	dp = [0] + [MAX] * amount
	#print(dp)

	for i in range(1, amount+1):
		calc = [dp[i-c] if i-c >= 0 else MAX for c in coins]
		print('calc: {}, adding {}+1'.format(calc, min(calc)))
		dp[i] = min(calc) + 1
		print(dp)

	return [dp[amount], -1][dp[amount] == MAX]

print(change([1,2,5], 11)) # 5+5+1 -> 3
print(change([1,3,4,8,11], 21)) # 11+8+1+1 -> 4 | 8+8+4+1 -> 4


