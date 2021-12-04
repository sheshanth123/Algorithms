
time O(n+m)
space O(n+m)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoListsHelper(self, list1, list2):
        if list1 is None and list2 is None:
            return None
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val > list2.val:
            list2.next = self.mergeTwoListsHelper(list1, list2.next)
            return list2
        list1.next = self.mergeTwoListsHelper(list1.next, list2)
        return list1
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeTwoListsHelper(list1, list2)
