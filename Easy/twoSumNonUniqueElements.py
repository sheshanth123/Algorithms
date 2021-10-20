# time O(n)
# space O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsDict = {}
        
        lenNums = len(nums)
        
        for numIndex in range(lenNums):
            numsDict[nums[numIndex]] = numIndex
            
        
        for elemIndex in range(len(nums)):
            secondElem = target - nums[elemIndex]
            
            if numsDict.get(secondElem) is not None and numsDict[secondElem] != elemIndex:
                return [elemIndex, numsDict[secondElem]]
