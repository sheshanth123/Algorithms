
#time -> O(n)
#space -> O(1)
class Solution:
    #{[()]}
    
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        mapping = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if char in mapping:
                topMostElement = stack.pop() if stack else '#'
                if topMostElement != mapping[char]:
                    return False
            else:
                stack.append(char)
        if len(stack)>0:
            return False
        return True
      
     
