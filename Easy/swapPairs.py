#time O(n)
#space O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapHelper(self, head):
        if head == None or head.next == None:
            return
        
        head.val, head.next.val = head.next.val, head.val
        self.swapHelper(head.next.next)
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.swapHelper(head)
        return head
