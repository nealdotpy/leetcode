'''
2. Add Two Numbers - Medium
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

Example:
	Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
	Output: 7 -> 0 -> 8
	Explanation: 342 + 465 = 807.
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Node, l2: Node) -> Node:
	n1 = ''
	n2 = ''
	while l1 != None:
		n1 += str(l1.val)
		l1 = l1.next

	while l2 != None:
		n2 += str(l2.val)
		l2 = l2.next

	n1=n1[::-1]; n2=n2[::-1]

	total = str(int(n1) + int(n2))
	#total[::-1]

	last = Node(int(total[0]))
	total = total[1:]
	temp = last
	while len(total):
		new = Node(int(total[0]), temp)
		temp = new
		total = total[1:]

	#print(n1, n2, total)

	return temp


a=Node(8);b=Node(1, a);			c=Node(2, b)
x=Node(0);						y=Node(6, x);z=Node(5, y)


node = addTwoNumbers(b, x)

while node != None:
	print('{} ->'.format(node.val), end= ' ')
	node = node.next

print('end')
