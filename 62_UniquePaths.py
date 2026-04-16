class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*(n+1) for i in range(m+1)]

        def backtrack(row, col):
            if row == 1 or col == 1:
                dp[row][col] = 1
                return 1
            if dp[row][col] != -1:
                return dp[row][col]
            
            dp[row][col] = backtrack(row - 1, col) + backtrack(row, col - 1)
            return dp[row][col]
        
        backtrack(m , n)
        return dp[-1][-1]