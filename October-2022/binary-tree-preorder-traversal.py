# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversalHelper(self, root, result):
        if root:
            result.append(root.val)
            self.preorderTraversalHelper(root.left, result)
            self.preorderTraversalHelper(root.right, result)
            
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        self.preorderTraversalHelper(root, result)
        return result
        
