'''
148. Sort List
https://leetcode.com/problems/sort-list/
Sort a linked list in O(n log n) time using constant space complexity.
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct_LL(array):
	if not array: return None
	head = Node(array[0]) # head
	ptr = head
	for element in array[1:]:
		new_node = Node(element)
		ptr.next = new_node
		ptr = ptr.next

	return head

# 392 ms (14.88%), 27 MB (6.88%)
def sort_list(head):
	# convert to unsorted array -> O(n)
	# sort unsorted array -> O(n log n) ==> merge/quicksort
	# convert sorted array to linked list -> O(n)
	unsorted_array = []
	while head != None:
		unsorted_array.append(head.val)
		head = head.next

	def merge_sort(to_be_sorted):
		if len(to_be_sorted) <= 1:
			return to_be_sorted

		left = []
		right = []
		for i, element in enumerate(to_be_sorted):
			if i < len(to_be_sorted) // 2:
				left.append(element)
			else:
				right.append(element)

		left = merge_sort(left)
		right = merge_sort(right)

		return merge(left, right)

	def merge(left_list, right_list):
		resulting_list = []

		while left_list and right_list:
			if left_list[0] <= right_list[0]:
				resulting_list.append(left_list[0])
				left_list.pop(0)
			else:
				resulting_list.append(right_list[0])
				right_list.pop(0)

		while left_list:
			resulting_list.append(left_list[0])
			left_list.pop(0)
		while right_list:
			resulting_list.append(right_list[0])
			right_list.pop(0)

		return resulting_list

	sorted_array = merge_sort(unsorted_array)

	sorted_LL = construct_LL(sorted_array)

	print(unsorted_array)
	print(sorted_array)

	return sorted_LL

# 340 ms (23.85%), 47.4 MB (5.09%)
def sort_list_merge_sort_for_linked_lists(head):

	def merge_sort_helper(left_node, right_node):
		resulting_list = None
		if not left_node: return right_node
		if not right_node: return left_node

		if left_node.val <= right_node.val:
			resulting_list = left_node
			resulting_list.next = merge_sort_helper(left_node.next, right_node)
		else:
			resulting_list = right_node
			resulting_list.next = merge_sort_helper(left_node, right_node.next)
		return resulting_list

	def get_middle_of_linked_list(head):
		if head == None:
			return head

		slow = fast = head
		while fast.next != None and fast.next.next != None:
			slow = slow.next
			fast = fast.next.next

		return slow

	if head == None or head.next == None:
		return head

	middle_node = get_middle_of_linked_list(head)
	middle_node_next = middle_node.next

	middle_node.next = None

	left_node = sort_list_merge_sort_for_linked_lists(head)
	right_node = sort_list_merge_sort_for_linked_lists(middle_node_next)

	return merge_sort_helper(left_node, right_node)

# 240 ms (66.53%), 23 MB (59.31%)
def sort_list_merge_sort_better(head):
	def merge(left_node, right_node):
		dummy = tail = ListNode(None)
		while left_node and right_node:
			if left_node.val < right_node.val:
				tail.next, tail, left_node = left_node, left_node, left_node.next
			else:
				tail.next, tail, right_node = right_node, right_node, right_node.next

		tail.next = left_node or right_node # the one extra one

		return dummy.next

	if not head or not head.next:
		return head

	pre, slow, fast = None, head, head
	while fast and fast.next:
		pre, slow, fast = slow, slow.next, fast.next.next
	pre.next = None # curtails to make 2 lists seperated at the middle

	return merge(*map(sort_list_merge_sort_better, (head, slow)))




print(sort_list(construct_LL([4, 2, 1, 3])))