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
    def preorderHelper(self, root):
        if root is None:
            return []
        
        nodes = [root.val]
        for child in root.children:
            nodes.extend(self.preorderHelper(child))
        return nodes
    
    def preorder(self, root: 'Node') -> List[int]:
        return self.preorderHelper(root)
