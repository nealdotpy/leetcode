'''
559. Maximum Depth of N-ary Tree - Easy
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
'''

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def maxDepth(root: TreeNode, level: int) -> int:
	if not root: return 0
	return 1 + max(map(self.maxDepth, root.children or [None]))