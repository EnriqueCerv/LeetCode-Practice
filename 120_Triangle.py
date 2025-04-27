def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        nRows = len(triangle)
        paths = [[-1]*len(row) for row in triangle]
        
        def backtrack(row, col):
            if row >= nRows:
                return 0
            if col >= len(triangle[row]):
                return float('inf')
            
            if paths[row][col] != -1:
                return paths[row][col]
            
            down = backtrack(row + 1, col)
            right = backtrack(row + 1, col + 1)

            paths[row][col] = triangle[row][col] + min(down, right)
            return paths[row][col]

        backtrack(0,0)
        return paths[0][0]


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