# time O(n)
# space O(n)
# bottom up approach
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        lenCost = len(cost)+1
        
        dp = [0] * lenCost
        
        for elemIndex in range(2, lenCost):
            dp[elemIndex] = min(dp[elemIndex-1]+ cost[elemIndex-1], \
                               dp[elemIndex-2]+ cost[elemIndex-2])
        return dp[-1]
    
# top down approach
class Solution:
    
    def dp(self, cost, currIndex, memoize):
        if currIndex < 2:
            return 0      
        if memoize.get(currIndex) is None:
            memoize[currIndex] = min(self.dp(cost, currIndex-1, memoize)+cost[currIndex-1], \
                                    self.dp(cost, currIndex-2, memoize)+cost[currIndex-2])          
        return memoize[currIndex]
    
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memoize = {} 
        top = len(cost)      
        return self.dp(cost, top , memoize)
