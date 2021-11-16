# time O(n^2)
# space O(n)
class Solution:
    
    def flip(self, arr, k):
        elemIndex = 0
        
        while elemIndex < k/2:
            arr[elemIndex], arr[k-elemIndex] = arr[k-elemIndex], arr[elemIndex]
            elemIndex += 1
            
    def pancakeSort(self, arr) :
        
        valueToSort = len(arr)
        
        ans = []
        
        while valueToSort > 0:
            indexOfValueToSort = arr.index(valueToSort)
            
            if indexOfValueToSort != valueToSort -1:
                if indexOfValueToSort != 0:
                    ans.append(indexOfValueToSort+1)
                    self.flip(arr, indexOfValueToSort)
                ans.append(valueToSort)
                self.flip(arr, valueToSort-1)
            valueToSort -= 1
        return ans
