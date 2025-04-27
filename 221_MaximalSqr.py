def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0]) # Get the dimensions of the matrix
        dp = [[0] * (cols + 1) for _ in range(rows + 1)] # Initialize DP table with extra row and column
        max_side_length = 0 # Maximum side length of a square of '1's

        for row in range(rows):
            for col in range(cols):
                # Check if the current element is a '1'
                if matrix[row][col] == '1':
                    # Update the DP table by considering the top, left, and top-left neighbors
                    dp[row + 1][col + 1] = min(
                        dp[row][col + 1],     # Top
                        dp[row + 1][col],     # Left
                        dp[row][col]          # Top-Left
                    ) + 1
                    # Update the max side length found so far
                    max_side_length = max(max_side_length, dp[row + 1][col + 1])
            print(dp)
      
        # Return the area of the largest square
        return max_side_length * max_side_length  