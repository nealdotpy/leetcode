# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, start: int, end: int) -> ListNode:
        if not head: return
        if start == end: return head
        fakeNode = ListNode(0)
        fakeNode.next = head

        current_node, previous_node = head, fakeNode

        # start-1
        for i in range(start-1): # O(start) O(N) | start is start pos, 
            current_node = current_node.next
            previous_node = previous_node.next

        # end-start, 
        for i in range(end-start): # O(end-start), O(N) | N len(head)
            temporary_node = current_node.next
            current_node.next = temporary_node.next
            temporary_node.next = previous_node.next
            previous_node.next = temporary_node
            
        return fakeNode.next