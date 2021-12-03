# time O(n)
# space O(n)

class Solution:
    def climbStairsHelper(self, n, memoize):
        if n==0 or n==1:
            return n
        
        if memoize.get(n) is None:
            memoize[n] = self.climbStairsHelper(n-1, memoize) + self.climbStairsHelper(n-2, memoize)
            
        return memoize[n]
    
    def climbStairs(self, n: int) -> int:
        
        memoize = {}
        
        return self.climbStairsHelper(n+1, memoize)
