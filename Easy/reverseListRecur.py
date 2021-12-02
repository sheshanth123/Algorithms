#time O(n)
#space O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListHelper(self, head, prev):
        if head == None:
            return prev
        
        nextNode = head.next
        head.next = prev
        
        return self.reverseListHelper(nextNode, head)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListHelper(head, None)
        
