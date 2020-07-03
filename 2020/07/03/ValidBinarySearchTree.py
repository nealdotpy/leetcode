

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.right = right
		self.left = left

def isValidBST(root : TreeNode, lo=float('-inf'), hi=float('inf')) -> bool:

	if not root:
		return True

	if not lo < root.val < hi:
		return False

	return self.isValidBST(root.left, lo, min(root.val, hi)) and \
			self.isValidBST(root.right, max(lo, root.val), hi)

# had to be done on website since dependent functions

print(isValidBST([5,1,4,None,None,3,6]))