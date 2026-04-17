class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        reachability = [[False]*n for _ in range(m)]
        
        def dfs(row, col, visited):
            nonlocal pacific, atlantic
            visited.add((row, col))

            if reachability[row][col]:
                atlantic = pacific = True

            if row == 0 or col == 0:
                pacific = True
            if row == m - 1 or col == n - 1:
                atlantic = True
            
            if pacific and atlantic:
                return

            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol

                if 0 <= nrow < m and 0 <= ncol < n and heights[nrow][ncol] <= heights[row][col] and (nrow, ncol) not in visited:
                    dfs(nrow, ncol, visited)
    
        
        ans = []
        for row in range(m):
            for col in range(n):
                pacific = atlantic = False
                dfs(row, col, set())
                if pacific and atlantic:
                    ans.append([row, col])
                    reachability[row][col] = True
        
        return ans
    

    class Solution:
        def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
            m, n = len(heights), len(heights[0])
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            
            def dfs(row, col, visited):
                visited.add((row, col))

                for drow, dcol in directions:
                    nrow, ncol = row + drow, col + dcol

                    if 0 <= nrow < m and 0 <= ncol < n and (nrow, ncol) not in visited and heights[nrow][ncol] >= heights[row][col]:
                        dfs(nrow, ncol, visited)
            
            pacific, atlantic = set(), set()

            for row in range(m):
                dfs(row, 0, pacific)
                dfs(row, n - 1, atlantic)
            for col in range(n):
                dfs(0, col, pacific)
                dfs(m - 1, col, atlantic)
            
            return [[row, col] for row in range(m) for col in range(n) if (row, col) in pacific and (row, col) in atlantic]