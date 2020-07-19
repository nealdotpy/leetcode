'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val;
		self.right = right
		self.left = left

def maxDepth(root: TreeNode, level: int) -> int:
	if not root: return 0
	return 1 + max(root.left, root.right)
	# return 1 + max(map(self.maxDepth, [root.left, root.right] or [None]))

