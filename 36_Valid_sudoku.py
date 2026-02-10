def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter
        import numpy as np

        board_T = np.array(board).T.tolist()

        for i in range(9):
            d = Counter(board[i])
            if any(val for key, val in d.items() if key != '.' and val > 1):
                return False

            d = Counter(board_T[i])
            if any(val for key, val in d.items() if key != '.' and val > 1):
                return False
        
        def square(i,j):
            arr = []
            for row in range(3):
                for col in range(3):
                    arr.append(board[i + row][j + col])
            d = Counter(arr)
            return any(val for key, val in d.items() if key != '.' and val > 1)
        
        for row in range(3):
            for col in range(3):
                if square(3*row, 3*col):
                    return False
        
        return True



def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter

        for row in range(9):
            freq = Counter()
            for col in range(9):
                num = board[row][col]
                freq[num] += 1
                if num != '.' and freq[num] > 1:
                    return False
        
        for col in range(9):
            freq = Counter()
            for row in range(9):
                num = board[row][col]
                freq[num] += 1
                if num != '.' and freq[num] > 1:
                    return False
        
        for i in range(3):
            for j in range(3):
                row, col = 3*i, 3*j
                freq = Counter()

                for i2 in range(3):
                    for j2 in range(3):
                        new_row = row + i2
                        new_col = col + j2
                        num = board[new_row][new_col]
                        freq[num] += 1
                        if num != '.' and freq[num] > 1:
                            return False
        
        return True