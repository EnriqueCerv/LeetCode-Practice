# %%
def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        paths = [[-1]*n for i in range(m)]

        def backtrack(i,j):
            if i == m - 1 and j == n - 1:
                paths[i][j] = grid[i][j]
                return grid[i][j]
            if i >= m or j >= n:
                return float('inf')
            
            if paths[i][j] != -1:
                return paths[i][j]
            
            right = backtrack(i, j + 1)
            down = backtrack(i + 1, j)
            paths[i][j] = grid[i][j] + min(right, down)
            return paths[i][j]
        
        backtrack(0,0)
        return paths[0][0]
# %%

## Tabulation approach
        # m, n = len(grid), len(grid[0])
        # paths = [[0]*n for i in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             paths[i][j] = grid[i][j]
        #         elif i == 0:
        #             paths[i][j] = grid[i][j] + paths[i][j - 1]
        #         elif j == 0:
        #             paths[i][j] = grid[i][j] + paths[i - 1][j]
        #         else:
        #             if paths[i - 1][j] < paths[i][j-1]:
        #                 path = paths[i - 1][j]
        #             else:
        #                 path = paths[i][j - 1]

        #             paths[i][j] = grid[i][j] + path

        # return paths[-1][-1]