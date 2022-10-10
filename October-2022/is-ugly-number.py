class Solution:
    def maxDivide(self, a, b):
        while a%b == 0:
            a = a/b
        return a
    
    def isUgly(self, n: int) -> bool:
        
        if n==0:
            return False
        no = self.maxDivide(n, 2)
        no = self.maxDivide(no, 3)
        no = self.maxDivide(no, 5)
        
        return no == 1
