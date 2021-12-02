#space O(n)
#time O(n)

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
        
        if val < root.val:
            return self.searchBSTHelper(root.left, val)
        return self.searchBSTHelper(root.right, val)
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        return self.searchBSTHelper(root, val)
        
# using iteration
# time O(n)
# space O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root
        
