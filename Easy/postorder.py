# time O(n)
# space O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorderHelper(self, root):
        if root is None:
            return []
        
        if root.children is None:
            return root.val
        
        nodes = []
        
        for child in root.children:
            nodes.extend(self.postorderHelper(child))
        nodes.append(root.val)
        return nodes
        
    
    def postorder(self, root: 'Node') -> List[int]:
        return self.postorderHelper(root)
        
