class Solution:
    def sortedSquares(self, nums ) :
        
        #[-4,-1,0,3,10]
        
        lenNums = len(nums)
        
        left = 0
        
        right = lenNums-1
        
        result = [0]*lenNums
        
        for elemIndex in range(lenNums-1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                square = nums[right]
                right -=1
            else:
                square = nums[left]
                left += 1
            result[elemIndex] = square * square
           
        return result

sol = Solution()
nums = [-4,-1,0,3,10]
output = sol.sortedSquares(nums)
print(output)
