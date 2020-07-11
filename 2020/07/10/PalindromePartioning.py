'''
131. Palindrome Partitioning - Medium
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:
	Input: "aab"
	Output:
	[
	  ["aa","b"],
	  ["a","a","b"]
	]
'''

def part(s: str):
	
	''' -> found all possible paritions in 1 array.
	if not s: return [[]]

	def find(s, l, r):
		res = []
		while l>=0 and r<len(s) and s[l] == s[r]:
			res.append(s[l:r+1])
			l -= 1
			r += 1
		return s[l+1:r]

	res = []
	for i in range(len(s)):
		odd = find(s, i, i); even = find(s, i, i+1)
		if odd: res += [odd]# odd length
		if even: res += [even] # even length

	print(res) 
	'''

	def pal(s: str) -> bool:
		return s == s[::-1] # self-expl

	def dfs(s, path, res):
		if not s:
			res.append(path)
			return
		for i in range(1, len(s)+1): # because we got from [:i] which is a [x,y) operation
			if pal(s[:i]): # if s up to substring i is a palindrome
				dfs(s[i:], path+[s[:i]], res)

	res = []
	dfs(s, [], res)
	return res

print(part('tytpp'))
