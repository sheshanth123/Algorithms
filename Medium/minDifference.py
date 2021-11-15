
#time -> O(nlogn)
#space -> O(1)
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        lenNums = len(nums)
        if lenNums < 4:
            return 0
        
        nums.sort()
        
        window = lenNums -3-1
        
        minDiff = float('inf')
        elemIndex = 0
        
        while elemIndex < lenNums:
            if (window+elemIndex) >= lenNums:
                break
                
            currMin = nums[window+elemIndex] - nums[elemIndex]
            minDiff = min(minDiff, currMin)
            
            elemIndex += 1
        return minDiff
