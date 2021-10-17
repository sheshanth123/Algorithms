# running Kadanes algo twice
# time -> O(n)

# space -> O(1)

class Solution:
    def maxAbsoluteSum(self, nums) -> int:
        currMin = nums[0]
        currMax = nums[0]
        
        maxSum = nums[0]
        minSum = nums[0]

        lenNums = len(nums)

        for elemIndex in range(1, lenNums):
            prevSum = currMax + nums[elemIndex]
            currElem = nums[elemIndex]
            currMax = max(prevSum, currElem)
            maxSum = max(maxSum, currMax)
        
        for elemIndex in range(1, lenNums):
            prevSum = currMin + nums[elemIndex]
            currElem = nums[elemIndex]
            currMin = min(prevSum, currElem)
            minSum = min(minSum, currMin)

        return max(abs(minSum), abs(maxSum))
