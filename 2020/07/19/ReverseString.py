'''
344. Reverse String - Easy
https://leetcode.com/problems/reverse-string/
'''

def rev_in_place(string) -> None:
	middle_index = len(string) // 2
	range_for_reverse = middle_index + 1 if len(string) % 2 else middle_index

	# DRY:
	# if len(string) % 2: # odd
	# 	for i in range(middle_index+1):
	# 		temp = string[i]
	# 		string[i] = string[-i-1]
	# 		string[-i-1] = temp
	# else: # even
	# 	for i in range(middle_index):
	# 		temp = string[i]
	# 		string[i] = string[-i-1]
	# 		string[-i-1] = temp

	for i in range(middle_index):
		temp = string[i]
		string[i] = string[-i-1]	
		string[-i-1] = temp	


A = ["h","e","l","l","o"]
B = ["H","a","n","n","a","h"]

print(A)
print(B)

rev_in_place(A)
rev_in_place(B)

print(A)
print(B)