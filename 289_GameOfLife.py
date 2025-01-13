
# %%
def gameOfLife(board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        def adjPositions(row, col, m ,n):
            adjIdx = []
            adjIdx += [[row - 1 , col + i] for i in range(-1,2) if row - 1 >= 0 and col + i >= 0 and col + i < n]
            adjIdx += [[row , col + i] for i in range(-1,2) if col + i >= 0 and col + i < n]
            adjIdx += [[row + 1 , col + i] for i in range(-1,2) if row + 1 < m and col + i >= 0 and col + i < n]
            adjIdx.pop(adjIdx.index([row, col]))
            return adjIdx

        m = len(board)
        n = len(board[0])
        onesBoard = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                adjIdx = adjPositions(i, j, m, n)
                nOnes = 0
                for adj in adjIdx:
                    adjRow = adj[0]
                    adjCol = adj[1]
                    if board[adjRow][adjCol] == 1:
                        nOnes += 1
                onesBoard[i][j] = nOnes
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if onesBoard[i][j] < 2:
                        board[i][j] = 0
                    elif onesBoard[i][j] > 3:
                        board[i][j] = 0
                else:
                    if onesBoard[i][j] == 3:
                        board[i][j] = 1

        return board

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
gameOfLife(board)
