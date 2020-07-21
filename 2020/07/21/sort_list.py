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



print(sort_list(construct_LL([4, 2, 1, 3])))