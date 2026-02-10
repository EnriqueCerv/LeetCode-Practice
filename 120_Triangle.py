def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        paths = [0]*(n+1)

        for row in reversed(range(n)):
            for col in range(row + 1):
                paths[col] = min(paths[col], paths[col + 1]) + triangle[row][col]

        return paths[0]


def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        paths = {}
        
        def backtrack(row, col):
            if row == n:
                return 0
            if col > row:
                return float('inf')
            if (row, col) in paths:
                return paths[(row, col)]
            
            down = backtrack(row + 1, col)
            right = backtrack(row + 1, col + 1)
            paths[(row, col)] = triangle[row][col] + min(down, right)
            return paths[(row, col)]
        
        return backtrack(0,0)

## bottom up approach
def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*n for _ in range(n)]

        for col in range(n):
            dp[-1][col] = triangle[-1][col]
        
        for row in reversed(range(n - 1)):
            for col in range(row + 1):
                path = min(dp[row + 1][col], dp[row + 1][col + 1])
                dp[row][col] = triangle[row][col] + path
        
        return dp[0][0]

## memoizzed approach
def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1]*n for i in range(n)]

        def rec(row, col):
            if row == n:
                return 0
            if col > row:
                return float('inf')
            if dp[row][col] != -1:
                return dp[row][col]
            
            down = rec(row + 1, col)
            right = rec(row + 1, col + 1)
            dp[row][col] = triangle[row][col] + min(down, right)
            return dp[row][col]
        
        return rec(0,0)
