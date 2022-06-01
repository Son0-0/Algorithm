# https://leetcode.com/problems/number-of-islands

class Solution:
    def __init__(self):
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def dfs(self, row, col, _map):
        for i in range(4):
            nx, ny = row + self.dx[i], col + self.dy[i]
            if 0 <= nx < len(_map) and 0 <= ny < len(_map[0]):
                if _map[nx][ny] == '1':
                    _map[nx][ny] = '0'
                    self.dfs(nx, ny, _map)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        cnt = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    grid[i][j] == '0'
                    self.dfs(i, j, grid)
                    cnt += 1
                    
        return cnt