#time O(n)
#space O(n)

#top down approach
class Solution:
    
    def robHelperMethod(self, nums, numsIndex, memoize):
        if numsIndex == 0:
            return nums[0]
        
        if numsIndex == 1:
            return max(nums[0], nums[1])
        
        if memoize.get(numsIndex) is None:
            memoize[numsIndex] = max(self.robHelperMethod(nums, numsIndex-1, memoize), self.robHelperMethod(nums, numsIndex-2, memoize)+nums[numsIndex])
            
        return memoize[numsIndex]
    
    
    def rob(self, nums: List[int]) -> int:
        memoize = {}
        
        lenNums = len(nums)
        
        return self.robHelperMethod(nums, lenNums-1, memoize)
    
#bottom up

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        lenNums = len(nums)
        
        if lenNums == 1:
            return nums[0]
        
        if lenNums == 2:
            return max(nums[0], nums[1])
        
        dp  =[0]* lenNums
        
        dp[0] = nums[0]
        
        dp[1] = max(nums[0], nums[1])
        
        for numsIndex in range(2, lenNums):
            dp[numsIndex] = max(dp[numsIndex-1], dp[numsIndex-2]+nums[numsIndex])
            
        return dp[-1]
