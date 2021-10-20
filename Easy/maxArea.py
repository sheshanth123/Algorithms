class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        leftIndex = 0
        rightIndex = len(height) - 1
        
        area = 0
        
        while rightIndex > leftIndex:
            valAtR = height[rightIndex]
            valAtL = height[leftIndex]
            
            length = min(valAtR, valAtL)
            
            width = rightIndex - leftIndex
            
            area = max(area, length * width)
            
            if valAtR > valAtL: 
                leftIndex += 1 
            else: 
                rightIndex -= 1
                    
        return area
