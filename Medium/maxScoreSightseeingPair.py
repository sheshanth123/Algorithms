# time O(n)
# space O(1)
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        lenValues = len(values)
        left = 0
        
        res = 0
        
        for elemIndex in range(lenValues):
            res = max(res, left + values[elemIndex] - elemIndex)
            left = max(left, values[elemIndex] + elemIndex)
        return res
