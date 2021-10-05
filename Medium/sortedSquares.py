class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        less = True
        lenA = len(nums)
        
        for elemIndex in range(lenA-1):
            if less:
                if nums[elemIndex] > nums[elemIndex+1]:
                    nums[elemIndex] ,nums[elemIndex+1] = nums[elemIndex+1] , nums[elemIndex]
            else:
                if nums[elemIndex] < nums[elemIndex+1]:
                    nums[elemIndex] , nums[elemIndex+1] = nums[elemIndex+1] , nums[elemIndex]
            less = not less
