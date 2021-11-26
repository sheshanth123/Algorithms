# time O(n)
# space O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        lenCost = len(cost)+1
        
        dp = [0] * lenCost
        
        for elemIndex in range(2, lenCost):
            dp[elemIndex] = min(dp[elemIndex-1]+ cost[elemIndex-1], \
                               dp[elemIndex-2]+ cost[elemIndex-2])
        return dp[-1]
