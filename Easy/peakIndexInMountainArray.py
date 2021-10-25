# time -> O(n)
# space -> O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        lenArr = len(arr)
        
        for elemIndex in range(lenArr-1):
            if arr[elemIndex] > arr[elemIndex+1]:
                return elemIndex
        return lenArr-1

    
# time -> O(logn)
# space -> O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        lenArr = len(arr)
        leftIndex = 0
        rightIndex = lenArr-1
        
        while leftIndex <= rightIndex:
            mid = leftIndex + (rightIndex-leftIndex)//2
            
            if arr[mid] < arr[mid+1]:
                leftIndex = mid+1
            else:
                rightIndex = mid-1
        return leftIndex
