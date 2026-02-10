# %%
# number of ways to tile dominoes (2x1) in (2xn) grid
def tiling(n):
    ways = [-1]*n
    def backtrack(i):
        if i == n - 1:
            ways[i] = 1
            return 1
        elif i == n - 2:
            ways[i] = 2
        elif i == n:
            return 0
        if ways[i] != -1:
            return ways[i]
        
        ways[i] = backtrack(i + 1) + backtrack(i + 2)
        return ways[i]

    return backtrack(0)
# %%
tiling(4)