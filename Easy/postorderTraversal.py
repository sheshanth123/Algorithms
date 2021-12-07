# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def postorderTraversalHelper(self, root):
        if root is None:
            return
        leftVal = self.postorderTraversalHelper(root.left)
        rightVal = self.postorderTraversalHelper(root.right)
        nodes = []
        if leftVal:
            nodes.extend(leftVal)
        if rightVal:
            nodes.extend(rightVal)
        nodes.append(root.val)
        return nodes    
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversalHelper(root)
