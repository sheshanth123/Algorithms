# time O(n^2)
# space O(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        self.start = 0
        self.maxLen = 0
        
        lenS = len(s)
        
        for elemIndex in range(lenS):
            self.expandFromCentre(s, elemIndex, elemIndex)
            self.expandFromCentre(s, elemIndex, elemIndex+1)
        return s[self.start:self.maxLen+self.start]
        
        
    def expandFromCentre(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if self.maxLen < right - left - 1:
            self.maxLen = right - left - 1
            self.start = left + 1
            
        
