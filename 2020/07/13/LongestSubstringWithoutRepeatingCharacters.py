'''
3. Longest Substring Without Repeating Characters - Medium
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Example 1:	
	Input: "abcabcbb"
	Output: 3 
	Explanation: The answer is "abc", with the length of 3. 

Example 2:	
	Input: "bbbbb"
	Output: 1
	Explanation: The answer is "b", with the length of 1.

Example 3:	
	Input: "pwwkew"
	Output: 3
	Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
def lols(s: str) -> int:
	L = 0
	i = 0
	while i < len(s):
		ht = dict()
		res = ''
		while s[i] not in res:
			res += s[i]
			ht[s[i]] = i
			i += 1
			# print(i, res, ht, L)
			if i >= len(s): break
			elif s[i] in res:
				i = ht[s[i]] + 1
				break
		L = [L, len(res)][len(res) >= L]
		#ht[len(res)] = res
	# print(ht)
	return L



print(lols('abcabcbb'))
print(lols('bbbbb'))
print(lols('pwwkew'))
print(lols(''))
print(lols('p'))
print(lols('abcdefghijklmnopqrstuvwxyzz'))
print(lols('dvdf'))
print(lols('pwtslwkew'))
