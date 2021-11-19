#time O(NxM)
#space O(NxM)
class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        count = 0

        for rowIndex in range(len(grid)):
            for colIndex in range(len(grid[0])):
                if grid[rowIndex][colIndex] == '1':
                    self.dfs(grid, rowIndex, colIndex)
                    count += 1

        return count

    def dfs(self, grid, rowIndex, colIndex):
        if (rowIndex < 0) or (colIndex < 0) or (rowIndex >= len(grid)) or (colIndex >= len(grid[0])) or (grid[rowIndex][colIndex] != '1'):
            return
        
        grid[rowIndex][colIndex] = '#'
        self.dfs(grid, rowIndex+1, colIndex)
        self.dfs(grid, rowIndex-1, colIndex)
        self.dfs(grid, rowIndex, colIndex+1)
        self.dfs(grid, rowIndex, colIndex-1)
