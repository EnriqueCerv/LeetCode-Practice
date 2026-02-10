# %%
# Given an mxn grid containing empty spaces '.', blockers 'X', and guards '>','<','v','^' looking in the arrow direction, write
# a program that determines whether an assassin starting in the grid point with element 'A', can reach the bottom right corner
# without being detected by any guard. The guard line of sight continues until blocked by a blocker or another guard.


# %%
def can_reach(grid):
    m, n = len(grid), len(grid[0])

    guards = {'>': (0, 1), '<': (0, -1), 'v': (-1, 0), '^': (1, 0)}
    # Block LoS
    for row in range(m):
        for col in range(n):
            ele = grid[row][col]
            if ele == 'A':
                start = (row, col)
            
            elif ele in guards:
                dx, dy = guards[ele]
                new_row, new_col = row + dx, col + dy
                while 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == '.':
                    grid[new_row][new_col] = '1'
                    new_row += dx
                    new_col += dy

    # Turn all blockers into '1' for easier checks
    for row in range(m):
        for col in range(n):
            ele = grid[row][col]
            if ele in guards or ele == 'X':
                grid[row][col] = '1'

    # Do dfs
    visited = [[False]*n for i in range(m)]
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    can_reach = False

    def dfs(row, col):
        nonlocal can_reach
        if row == m - 1 and col == n - 1:
            can_reach = True
            return

        visited[row][col] = True
        for dx, dy in dir:
            new_row = row + dx
            new_col = col + dy

            if 0 <= new_row < m and 0 <= new_col < n:
                if not visited[new_row][new_col] and grid[new_row][new_col] != '1':
                    dfs(new_row, new_col)

    dfs(*start)
    return can_reach
        
# %%
grid1 = [
    ["A", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]
# Expected: Reachable
grid2 = [
    ["A", ".", ">"],
    [".", ".", "X"],
    [".", ".", "."]
]
# Expected: Reachable
grid3 = [
    ["A", ">", "."],
    [".", ".", "."],
    [".", ".", "."]
]
# Expected: Not reachable
grid4 = [
    ["A", ".", "X"],
    [".", ".", ">"],
    [".", ".", "."]
]
# Expected: Reachable
grid5 = [
    ["A", ".", ".", "X"],
    [">", ".", ".", "."],
    ["^", ".", ".", "."]
]
# Expected: Not reachable
grid6 = [
    ["A", ".", ".", "X", ".", "."],
    [".", "X", "v", "X", ".", "."],
    [".", ".", "X", ".", ".", "."]
]
# Expected: Reachable
grid7 = [
    ["A", ".", ".", ".", "."],
    [".", ".", ".", ".", "^"],
    [".", ".", ".", ".", ">"]
]
# Expected: Not reachable
grid8 = [
    ["A", ".", ".", ".", "."],
    [".", ".", ".", ".", "^"],
    [".", ".", ".", ".", "X"]
]
# %%
can_reach(grid8)