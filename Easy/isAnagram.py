
# using hashtable
# time -> O(n)
# space -> O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sCharDict = {}
        
        if s.__len__() != t.__len__():
            return False
        
        for char in s:
            if sCharDict.get(char) is not None:
                sCharDict[char] += 1
            else:
                sCharDict[char] = 1
        
        for char in t:
            if sCharDict.get(char):
                sCharDict[char] -= 1
            else:
                return False
        return True
        
#using counter array
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charCounter = [0]*126
        
        if s.__len__() != t.__len__():
            return False
        
        for char in s:
            charCounter[ord(char)] += 1
            
        for char in t:
            if charCounter[ord(char)]:
                charCounter[ord(char)] -= 1
            else:
                return False
        return True
        
