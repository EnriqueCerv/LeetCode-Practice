def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """"""
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        paths = [[-1]*n for i in range(m)]

        def backtrack(i,j):
            if i == m - 1 and j == n - 1:
                paths[i][j] = 1
                return 1
            if i >= m or j >= n:
                return 0

            if paths[i][j] != -1:
                return paths[i][j]
            
            if obstacleGrid[i][j] == 1:
                paths[i][j] = 0
                return 0
            else:
                paths[i][j] = backtrack(i+1, j) + backtrack(i, j+1)
                return paths[i][j]
            
        backtrack(0,0)
        return 0 if obstacleGrid[m-1][n-1] == 1 else paths[0][0]