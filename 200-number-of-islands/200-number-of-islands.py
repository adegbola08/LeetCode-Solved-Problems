class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        explored = set()
        
        
        for i in range(len(grid)):
            
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in explored:
                    self.explore(i, j, grid, explored)
                    count += 1
        
        return count
        
    def explore(self, r, c, grid, explored):
        row = 0 <= r and r < len(grid)
        col = 0 <= c and c < len(grid[0])
        
        if not row or not col:
            return False
        
        if (r,c) in explored:
            return False
        if grid[r][c] != "1":
            return False
        explored.add((r,c))
        
        self.explore(r-1, c, grid, explored)
        self.explore(r+1, c, grid, explored)
        self.explore(r, c-1, grid, explored)
        self.explore(r, c+1, grid, explored)
        
        return True