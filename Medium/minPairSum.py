# time O(nlogn)
# space O(1)

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        lenNums = len(nums)
        best = 0
        for elemIndex in range(lenNums//2):
            best = max(best, nums[elemIndex] + nums[lenNums-1-elemIndex])
        return best
