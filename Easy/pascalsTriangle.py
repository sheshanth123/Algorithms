# time O(n*2)
# space O(n*2)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = []
        
        for rowNum in range(numRows):
            row = [0] * (rowNum+1)
            
            row[0], row[-1] = 1, 1
            
            for col in range(1, len(row)-1):
                row[col] = triangle[rowNum-1][col-1] + triangle[rowNum-1][col]
            triangle.append(row)
            
        return triangle
    

# using recursion

class Solution:
    def generateHelper(self, numRows, currRow, triangle):
        if currRow == numRows:
            return triangle
        
        row = [0] * (currRow+1)
        
        row[0], row[-1] = 1,1
        
        for colNum in range(1, len(row)-1):
            row[colNum] = triangle[currRow-1][colNum-1] + triangle[currRow-1][colNum]
        triangle.append(row)
        return self.generateHelper(numRows, currRow+1, triangle)
    
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        self.generateHelper(numRows, 0, triangle)
        return triangle
            
        
