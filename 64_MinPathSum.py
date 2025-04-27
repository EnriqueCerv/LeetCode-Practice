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
def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)

