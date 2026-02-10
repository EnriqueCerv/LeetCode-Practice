class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            # print(row, col, '2')
            
            directions = [(0,1), (0, -1), (1,0), (-1,0)]
            grid[row][col] = 0

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == '1':
                    dfs(new_row, new_col) 
        
        m, n = len(grid), len(grid[0])
        n_islands = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    # print(row, col)
                    dfs(row, col)
                    n_islands += 1

        return n_islands