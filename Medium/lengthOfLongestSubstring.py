# time O(n)
# space O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charArr = [0] * 128
        
        leftIndex = 0
        rightIndex = 0
        
        result = 0
        
        lenS = len(s)
        
        while rightIndex < lenS:
            charAtR = s[rightIndex]
            
            charArr[ord(charAtR)] += 1
            
            while charArr[ord(charAtR)] > 1:
                charAtL = s[leftIndex]
                
                charArr[ord(charAtL)] -= 1
                
                leftIndex += 1
            
            result = max(result, rightIndex - leftIndex + 1)
            
            rightIndex += 1
            
        return result
            
            
        
