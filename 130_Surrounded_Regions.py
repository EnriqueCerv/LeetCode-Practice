class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def replace(row, col):
            board[row][col] = 'T'

            for dx, dy in directions:
                nrow, ncol = row + dy, col + dx

                if 0 <= nrow < m and 0 <= ncol < n and board[nrow][ncol] == 'O':
                    replace(nrow, ncol)

        for row in range(m):
            if board[row][0] == 'O':
                replace(row, 0)
            if board[row][-1] == 'O':
                replace(row, n - 1)
        
        for col in range(n):
            if board[0][col] == 'O':
                replace(0, col)
            if board[-1][col] == 'O':
                replace(m - 1, col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'T':
                    board[row][col] = 'O'
        
        return board

        