'''
234. Palindrome Linked List - Easy
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.
'''
class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def is_palindrome(head):

	# def reverse_linked_list(root):
	# 	if not root: return None
	# 	curr_node, prev_node, next_node = root, None, root.next
	# 	while curr_node != None:
	# 		next_node = curr_node.next
	# 		curr_node.next = prev_node
	# 		prev_node = curr_node
	# 		curr_node = next_node
	# 	# print(curr_node.val, curr_node.next)
	# 	return prev_node

	# # return reverse_linked_list(head)
	# forwards = head
	# backwards = reverse_linked_list(head)

	# print_LL(forwards)
	# print_LL(backwards)

	# while forwards != None:
	# 	if forwards.val != backwards.val:
	# 		return False
	# 	forwards = forwards.next
	# 	backwards = backwards.next
	# return True

	reverse = None
	slow = fast = head
	while fast and fast.next:
		fast = fast.next.next
		reverse, reverse.next, slow = slow, reverse, slow.next
	if fast: # end of list since 'fast and None' -> False from while loop
		slow = slow.next
	while reverse and reverse.val == slow.val:
		slow = slow.next
		reverse = reverse.next

	return not reverse


def construct_LL(array):
	if not array: return None
	head = Node(array[0]) # head
	ptr = head
	for element in array[1:]:
		new_node = Node(element)
		ptr.next = new_node
		ptr = ptr.next

	return head

LL = construct_LL([1, 2, 3, 2, 1])
LL_A = construct_LL([1, 2, 3, 3, 2, 1])
LL_A2 = construct_LL([1, 2, 3, 4, 2, 1])
LL_B = construct_LL([1])
LL_C = construct_LL(None)


# def print_LL(head):
# 	while head != None:
# 		print('{}->'.format(head.val), end='')
# 		head = head.next
# 	print()

# print_LL(LL)

print(is_palindrome(LL))
print(is_palindrome(LL_A))
print(is_palindrome(LL_A2))
print(is_palindrome(LL_B))
print(is_palindrome(LL_C))