'''
8. String to Integer (atoi) - Medium
https://leetcode.com/problems/string-to-integer-atoi/

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first 
non-whitespace character is found. Then, starting from this character, takes an optional 
initial plus or minus sign followed by as many numerical digits as possible, and interprets 
them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace 
characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Notes:
* 	Only the space character ' ' is considered as whitespace character.
* 	Assume we are dealing with an environment which could only store integers within the 32-bit 
	signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of 
	representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
'''

def my_atoi(str) -> int:
	dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
			'6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
	INT_MIN = -1 * 2 ** 31
	INT_MAX =  2 ** 31 - 1
	negative = False
	stack = []
	nums = 0
	ans = 0
	if len(str) == 0: return 0
	while str[0] == ' ' and len(str) > 1:
		str = str[1:]

	if str[0] == '-': 
		negative = True
		str = str[1:]
	elif str[0] == '+':
		str = str[1:]

	for char in str:
		try:
			#print('appending {}'.format(char))
			stack.append(dic[char])
			nums += 1
		except KeyError:
			if len(stack) == 0:
				return 0
			else:
				break
				# print('stop taking input!!')
				# print(stack)

	for digit in stack:
		#print('digit up: {}'.format(digit))
		nums -= 1
		ans += digit * (10 ** nums)

	ans = ans * (-1 if negative else 1)

	if ans > INT_MAX:
		ans = INT_MAX
	elif ans < INT_MIN:
		ans = INT_MIN

	return ans

	#print(str)
	#print(str.split(' ').remove(' '))

print(my_atoi('   -42 w'))
print(my_atoi('4193 with words'))
print(my_atoi('words and 987'))
print(my_atoi('-91283472332'))