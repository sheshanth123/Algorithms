# time -> O(n)
# space -> O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        lenArr = len(arr)
        
        for elemIndex in range(lenArr-1):
            if arr[elemIndex] > arr[elemIndex+1]:
                return elemIndex
        return lenArr-1
