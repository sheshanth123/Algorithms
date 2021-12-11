# time O(n)
# space O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque([root])
        
        nodes = []
        
        while queue:
            levelList = []
            
            lenQueue = len(queue)
            for _ in range(lenQueue):
                
                currNode = queue.popleft()
                levelList.append(currNode.val)
                queue.extend(currNode.children)
            
            nodes.append(levelList)
                
        return nodes
        
