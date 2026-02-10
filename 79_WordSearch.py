# %%
def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row, col, cur_word):
            letter = board[row][col]
            cur_word += letter
            board[row][col] = '0'

            if not word.startswith(cur_word):
                board[row][col] = letter
                return False
            elif word == cur_word:
                return True

            directions = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for new_row, new_col in directions:
                if 0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] != '0':
                    if dfs(new_row, new_col, cur_word):
                        return True
            
            board[row][col] = letter
            return False
        
        m = len(board)
        n = len(board[0])

        for row in range(m):
            for col in range(n):
                if dfs(row, col, ''):
                    return True

        return False