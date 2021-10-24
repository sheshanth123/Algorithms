# time O(log n)
# space O(1)

class Solution:
    def searchRange(self, nums, target) :
        
        rngLow = -1
        rngHigh = -1


        lenNums = len(nums)
        
        if lenNums == 0 or (lenNums == 1) and (nums[0] != target):
            return [rngLow, rngHigh]
        
        elif lenNums == 1:
            return [0,0]

        leftIndex = 0
        rightIndex = lenNums - 1

        
        while leftIndex <= rightIndex:
            mid = leftIndex + (rightIndex-leftIndex)//2

            if (nums[mid] > target) or ((nums[mid] == target) and mid > 0 and nums[mid]==nums[mid-1]):
                rightIndex -= 1
            elif nums[mid] == target:
                rngLow = mid
                break
            else:
                leftIndex += 1
        
        leftIndex = 0
        rightIndex = lenNums-1
        
        while leftIndex <= rightIndex:
            mid = leftIndex + (rightIndex - leftIndex)//2

            if (nums[mid] < target) or ((nums[mid]==target) and (mid<(lenNums-1)) and (nums[mid] == nums[mid+1])):
                leftIndex += 1
            elif nums[mid] == target:
                rngHigh = mid
                break
            else:
                rightIndex -= 1
        return [rngLow, rngHigh]
