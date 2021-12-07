# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversalHelper(self, root):
        if root is None:
            return
        
        nodes = []
        leftVal = self.inorderTraversalHelper(root.left)
        if leftVal:
            nodes.extend(leftVal)
            
        nodes.append(root.val)
        
        rightVal = self.inorderTraversalHelper(root.right)
        if rightVal:
            nodes.extend(rightVal)
            
        return nodes
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversalHelper(root)
