class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n//2):
            for col in range(n):
                matrix[row][col], matrix[n - row - 1][col] = matrix[n - row - 1][col], matrix[row][col]

        for row in range(n):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]