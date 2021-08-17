#used to increase the recursion limit
import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        lenStr = len(A)
        return self.isPalindrome(A, 0, lenStr-1)
        
    def isPalindrome(self, inpStr, start, stop):
        #base condition
        if start >= stop:
            return 1
        #everytime we need to make sure if the start and end charactors are same and also ensure is same for all
        elif (inpStr[start] == inpStr[stop]) & self.isPalindrome(inpStr, start+1, stop-1):
            return 1
        #for all other conditions return 0
        return 0
        
