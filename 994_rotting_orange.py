class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        m, n = len(grid), len(grid[0])
        queue, fresh = deque(), 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        mins = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            mins += 1
            for _ in range(len(queue)):
                crow, ccol = queue.popleft()

                for drow, dcol in directions:
                    nrow, ncol = crow + drow, ccol + dcol

                    if 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = 2
                        fresh -= 1
                        queue.append((nrow, ncol))

                        if fresh == 0:
                            return mins
                            
        return -1 if fresh > 0 else 0