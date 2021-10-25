# time -> O(nlogn)
# space -> O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        mergedArray = []
        
        for interval in intervals:
            if mergedArray.__len__() == 0 or mergedArray[-1][1] < interval[0]:
                mergedArray.append(interval)
            else:
                mergedArray[-1][1] = max(interval[1], mergedArray[-1][1])
        return mergedArray
