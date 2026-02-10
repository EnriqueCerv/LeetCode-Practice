
def solveNQueens(self, n: int) -> List[List[str]]:

        def dfs(row):
            if row == n:
                solution.append([''.join(row_state) for row_state in board])
                return
            
            for col in range(n):
                if column[col] == 0 and diag[row + col] == 0 and adiag[n - row + col] == 0:
                    board[row][col] = 'Q'
                    
                    column[col] = diag[row + col] = adiag[n - row + col] = 1

                    dfs(row + 1)

                    column[col] = diag[row + col] = adiag[n - row + col] = 0
                    board[row][col] = '.'

        board = [['.']*n for i in range(n)]
        solution = []
        column = [0]*n
        diag = [0]*(2*n)
        adiag = [0]*(2*n)

        dfs(0)
        return solution