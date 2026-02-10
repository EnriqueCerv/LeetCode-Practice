# %%
# Given an mxn grid containing empty spaces '.', blockers 'X', and guards '>','<','v','^' looking in the arrow direction, write
# a program that determines whether an assassin starting in the grid point with element 'A', can reach the bottom right corner
# without being detected by any guard. The guard line of sight continues until blocked by a blocker or another guard.

# %%
def can_reach(grid):
    m, n = len(grid), len(grid[0])
    guards = {'>':(0,1), '<':(-1,0), 'v':(1,0), '^':(-1,0)}

    for row in range(m):
        for col in range(n):
            val = grid[row][col]
            if val == 'A':
                start = (row, col)

            if val in guards:
                dy, dx = guards[val]

                new_col, new_row = col + dx, row + dy
                while 0 <= new_col < n and 0 <= new_row < m:
                    val = grid[new_row][new_col]
                    if val == '.':
                        grid[new_row][new_col] = '1'
                        new_row += dy
                        new_col += dx
                    else:
                        break

    for row in range(m):
        for col in range(n):
            val = grid[row][col]
            if val == 'X' or val in guards:
                grid[row][col] = '1'
    
    visited = [[False]*n for _ in range(m)]
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    can_reach = False

    def dfs(row, col):
        nonlocal can_reach

        if row == m-1 and col == n-1:
            if grid[row][col] != '1':
                can_reach = True
            return

        visited[row][col] = True
        for dx, dy in dir:
            new_row, new_col = row + dx, col + dy

            if 0 <= new_row < m and 0 <= new_col < n:
                if grid[new_row][new_col] != '1' and not visited[new_row][new_col]:
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
    [".", ">", ".", "^", "^"],
    [".", ".", ".", ".", "."]
]
# %%
can_reach(grid8)



# %%
# In a day, an account holder at HackerBank wants to make n transactions. 
# In each transaction, money is either sent (negative amount) or received (positive amount).
# Given n transactions, the transactions occur in order from 1 through n, but transactions may be skipped.
# The balance starts at 0 and is the running sum of the selected transactions. 
# It can never go negative. 
# Find out the maximum number of transactions possible. 

transactions = [3,2,-5,-6,-1,4]
# Should return 4 for for transactions 1,2,3,6.
# transactions = [-5, 10, -3, 7, -8, 2]
# Should return 5 for 10,-3,7,-8,2

# %%
def maxTransactions(nums):
    n = len(nums)
    seen_transactions = {}

    def backtrack(idx, balance):
        
        if idx == n:
            return  0
        if balance < 0:
            return 0
        if (idx, balance) in seen_transactions:
            return seen_transactions[(idx, balance)]
        
        do = 1 + backtrack(idx + 1, balance + nums[idx])
        skip = backtrack(idx + 1, balance)

        seen_transactions[(idx, balance)] = max(do, skip)
    
        return seen_transactions[(idx, balance)]

    return backtrack(0,0)

maxTransactions(transactions)
# %%
# %%
# Given n items where each item has some weight 
# and profit associated with it and also given a 
# bag with capacity W, 
# [i.e., the bag can hold at most W weight in it]. 
# The task is to put the items into the bag such that the 
# sum of profits 
# associated with them is the maximum possible. 

weight = [4,5,1]
profit = [1,2,3]
maxWeight = 4
# 3

profit = [60, 100, 120]
weight = [10, 20, 30]
maxWeight = 50
# # 220

profit = [10, 20, 30]
weight = [2, 3, 5]
maxWeight = 10
# # 60

profit = [100, 90, 120]
weight = [50, 40, 60]
maxWeight = 50
# # 100

def knapsack(weights, profit, maxWeight):
    seen = {}
    n = len(weights)
    def backtrack(idx, cur_weight):
        if idx == n or cur_weight > maxWeight:
            return 0
        if (idx, cur_weight) in seen:
            return seen[(idx, cur_weight)]

        take = 0
        if cur_weight + weights[idx] <= maxWeight:
            take = profit[idx] + backtrack(idx + 1, cur_weight + weights[idx])
        skip = backtrack(idx + 1, cur_weight)


        seen[(idx, cur_weight)] = max(take, skip)
        return seen[(idx, cur_weight)]

    return backtrack(0,0)
        

knapsack(weight, profit, maxWeight)