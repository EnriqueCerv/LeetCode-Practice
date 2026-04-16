class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def replace_by_zeros(row, col):
            for i in range(m):
                matrix[i][col] = 0
            for j in range(n):
                matrix[row][j] = 0
        
        m, n = len(matrix), len(matrix[0])
        zeros = [[0]*n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if not matrix[row][col]:
                    zeros[row][col] = 1
        
        for row in range(m):
            for col in range(n):
                if zeros[row][col]:
                    replace_by_zeros(row, col)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        locs = [(i,j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        
        def fill(row, col):
            for i in range(m):
                matrix[i][col] = 0
            for j in range(n):
                matrix[row][j] = 0
        
        for row, col in locs:
            fill(row, col)
        