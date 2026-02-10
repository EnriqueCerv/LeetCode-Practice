def totalNQueens(self, n: int) -> int:

        board = [['.']*n for i in range(n)]
        states = 0
        
        columns = [0]*n
        diag = [0]*(2*n)
        adiag = [0]*(2*n)
        
        def dfs(row):
            nonlocal states
            
            if row == n:
                states += 1

            for col in range(n):
                if columns[col] + diag[n - (row - col)] + adiag[row + col] == 0:
                    board[row][col] = 'Q'
                    columns[col] = diag[n - (row - col)] = adiag[row + col] = 1
                    dfs(row + 1)

                    board[row][col] = '.'
                    columns[col] = diag[n - (row - col)] = adiag[row + col] = 0

        dfs(0)

        return (states)