# time O(n! n)
# space O(n! n)
class Solution:
    def permuteHelper(self, nums, numsIndex, permutations):
        import copy
        if len(nums) == numsIndex:
            permutations.append(copy.deepcopy(nums))
            return
        else:
            for elemIndex in range(numsIndex, len(nums)):
                nums[elemIndex], nums[numsIndex] = nums[numsIndex], nums[elemIndex]
                self.permuteHelper(nums, numsIndex+1, permutations)
                nums[elemIndex], nums[numsIndex] = nums[numsIndex], nums[elemIndex]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permuteHelper(nums, 0, permutations)
        return permutations
