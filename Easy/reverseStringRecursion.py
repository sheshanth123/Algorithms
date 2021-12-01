#time O(n)
#space O(n)
class Solution:
    def helper(self, s, start, end):
        if start >= end:
            return
        
        s[start], s[end] = s[end], s[start]
        self.helper(s, start+1, end-1)
            
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        self.helper(s, 0, len(s)-1)
        
