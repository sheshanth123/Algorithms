# time O(log n)
# space O(log n)

class Solution:
    
    def myPowHelper(self, x, n):
        if n == 0:
            return 1
        
        half = self.myPowHelper(x, n//2)
        
        if n % 2 == 0:
            return half * half
        
        return half * half * x
    
    
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1/x
            n = -n
            
        return self.myPowHelper(x, n)
