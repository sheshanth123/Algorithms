"""
using stack
time O(M+N)
space O(M+N)
"""

class Solution:
    
    def buildStr(self, inpStr):
        newStr = []
        
        for char in inpStr:
            if char =='#':
                if len(newStr) == 0:
                    continue
                newStr.pop()
            else:
                newStr.append(char)
        return newStr
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.buildStr(s) == self.buildStr(t)
