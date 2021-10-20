# time O(k)
# space O(1)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        #[1,2,3,4,5,6,1]
        leftIndex = 0
        lenR = len(cardPoints)
        rightIndex = lenR - k
        kSum = 0
        
        for elemIndex in range(rightIndex, lenR):
            kSum += cardPoints[elemIndex]
            
        maxSum = kSum
        
        while rightIndex < lenR:
            kSum = kSum + cardPoints[leftIndex] - cardPoints[rightIndex]
            maxSum = max(maxSum, kSum)
            leftIndex += 1
            rightIndex += 1
        return maxSum
