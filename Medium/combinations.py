import copy
class Solution:
    def combineHelper(self, nums, buffer, startIndex, bufferIndex, permutations):
        if len(buffer) == bufferIndex:
            permutations.append(copy.deepcopy(buffer))
            return
        
        if len(nums) == startIndex:
            return
        
        for elemIndex in range(startIndex, len(nums)):
            buffer[bufferIndex] = nums[elemIndex]
            self.combineHelper(nums, buffer, elemIndex+1, bufferIndex+1, permutations)
        
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [elem for elem in range(1,n+1)]
        buffer = [0]*k
        permutations = []
        self.combineHelper(nums, buffer, 0, 0, permutations)
        return permutations
