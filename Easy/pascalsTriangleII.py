# time O(n*2)
# space O(n)

class Solution:
    def getRowHelper(self, rowIndex, currRow, triangle):
        
        if currRow == rowIndex+1:
            return triangle
        
        row = [0]* (currRow+1)
        
        row[0], row[-1] = 1,1
        
        for colNum in range(1, len(row)-1):
            row[colNum] = triangle[currRow-1][colNum-1] + triangle[currRow-1][colNum]
        triangle.append(row)
        
        return self.getRowHelper(rowIndex, currRow+1, triangle)
    
    
    def getRow(self, rowIndex: int) -> List[int]:
        
        triangle = []
        
        self.getRowHelper(rowIndex, 0, triangle)
        
        return triangle[rowIndex]
