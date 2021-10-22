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
    
    
"""
time O(M+N)
space O(1)
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        lenS = len(s) - 1
        lenT = len(t) - 1
        
        skipS = 0
        skipT = 0
        
        while lenS >= 0 or lenT >= 0:
            while lenS >= 0: 
                if s[lenS] == '#': 
                    lenS -=1
                    skipS +=1
                elif skipS > 0:
                    lenS -= 1
                    skipS -= 1
                else:
                    break
                    
                
            while lenT >= 0:
                if t[lenT] == '#':
                    skipT += 1
                    lenT -= 1
                elif skipT > 0:
                    lenT -= 1
                    skipT -= 1
                else:
                    break
            
            if lenT >= 0 and lenS >= 0 and (s[lenS] != t[lenT]):
                return False
            if (lenS >= 0) != (lenT>= 0):
                return False
            lenT -= 1
            lenS -= 1
        
        return True    
