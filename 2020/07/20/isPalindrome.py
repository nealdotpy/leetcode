'''
125. Valid Palindrome - Easy
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only 
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as 
valid palindrome.
'''
def isPalindrome(s: str) -> bool:
	if not s: return True

	# 0-9 [48,57] a-z[97,122]
	def clean(string_to_check):
		def valid_numeric(char):
			return 48 <= ord(char) <= 57

		def valid_alpha(char):
			return 97 <= ord(char) <= 122

		return ''.join([char if valid_numeric(char) or valid_alpha(char) else '' \
				for char in string_to_check.lower()])

	#print(clean(s))

	#return clean(s) == clean(s)[::-1] # -> optimize
	s = clean(s)
	mid = len(s) // 2
	l, r = (mid, mid) if len(s) % 2 else (mid-1, mid)
	# print(s)
	while l >= 0 and r < len(s):
		if s[l] != s[r]:
			return False
		l -= 1
		r += 1
	return True


A = '' # T
B = 'add' # F
C = 'A man, a plan, a canal: Panama' # T
D = 'race a car' # F
E = 'race car'

print(isPalindrome(A))
print(isPalindrome(B))
print(isPalindrome(C))
print(isPalindrome(D))

