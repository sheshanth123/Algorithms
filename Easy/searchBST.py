#time O(n)
#space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBSTHelper(self, root, val):
        if root is None:
            return None
        
        if root.val == val:
            return root
        left = self.searchBSTHelper(root.left, val)
        right = self.searchBSTHelper(root.right, val)
        
        if left:
            return left
        return right
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.searchBSTHelper(root, val)
        
