# %%
# In a day, an account holder at HackerBank wants to make 
# n transactions. 
# In each transaction, money is either sent (negative amount) 
# or received (positive amount).
# Given n transactions, the transactions occur in order 
# from 1 through n, but transactions may be skipped.
# The balance starts at 0 and is the running sum of 
# the selected transactions. 
# It can never go negative. 
# Find out the maximum number of transactions possible. 

transactions = [3,2,-5,-6,-1,4]
# Should return 4 for for transactions 1,2,3,6.
# transactions = [-5, 10, -3, 7, -8, 2]
# Should return 5 for 10,-3,7,-8,2

# %%
# Using dp

def max_trans(transactions):
    n = len(transactions)
    dp = {}

    def rec(idx, balance):
        if idx == n:
            return 0
        if balance < 0:
            return -float('inf')
        if (idx, balance) in dp:
            return dp[(idx, balance)]

        do = 1 + rec(idx + 1, balance + transactions[idx])
        skip = rec(idx + 1, balance)

        dp[(idx, balance)] = max(do, skip)
        return dp[(idx, balance)]

    return rec(0,0)

max_trans(transactions)
# %%
# Using heaps
import heapq

def max_trans(transactions):
    min_heap = []
    balance = 0

    for transaction in transactions:
        heapq.heappush(min_heap, transaction)
        balance += transaction

        if balance < 0:
            to_remove = heapq.heappop(min_heap)
            balance -= to_remove

    return len(min_heap)

max_trans(transactions)

   
# %%
# %%
# Given n items where each item has some weight 
# and profit associated with it and also given a 
# bag with capacity W, 
# [i.e., the bag can hold at most W weight in it]. 
# The task is to put the items into the bag such that the 
# sum of profits 
# associated with them is the maximum possible. 

def knapsack(weights, values, W):
    n = len(weights)
    dp = {}

    def rec(i, cur_weight):
        if i == n:
            return 0
        if (i, cur_weight) in dp:
            return dp[(i, cur_weight)]
        
        do = values[i] + rec(i + 1, cur_weight + weights[i]) if cur_weight + weights[i] <= W else 0
        skip = rec(i + 1, cur_weight)
        dp[(i, cur_weight)] = max(do, skip)
        
        return dp[(i, cur_weight)]
    
    return rec(0,0)
        


weights = [4,5,1]
values = [1,2,3]
W = 4
# 3

# values = [60, 100, 120]
# weights = [10, 20, 30]
# W = 50
# # 220

knapsack(weights, values, W)


# %%
# %%


# Given a string of length N containing '_' for empty space and 'H' for house. 
# Write a function that gives the minimum number of water tanks you can place.
# A house can collect water froma water tank if it is adjacent to it on the left 
# or on the right. 
# For example, S = '-H-HH--' should output two with the example 
# configuration '-HTHHT-' where T is a tank. 
# If not possible, return -1

def tanks(arr):
    n = len(arr)
    tanks = 0

    for idx, ele in enumerate(arr):
        if ele == 'H':
            if (idx - 1 >= 0 and arr[idx - 1] == 'T') or (idx + 1 < n and arr[idx + 1] == 'T'):
                continue
            
            if idx + 1 < n and arr[idx + 1] == '-':
                arr[idx + 1] = 'T'
                tanks += 1
            elif idx - 1 >= 0 and arr[idx - 1] == '-':
                arr[idx - 1] = 'T'
                tanks += 1
            else:
                return -1
    return tanks

a = list('-H-HH--')
a = list('-HH-H--H-H')
tanks(a)
            
# %%
# Given an mxn grid containing empty spaces '.', blockers 'X', and guards '>','<','v','^' looking in the arrow direction, write
# a program that determines whether an assassin starting in the grid point with element 'A', can reach the bottom right corner
# without being detected by any guard. The guard line of sight continues until blocked by a blocker or another guard.


def can_reach(grid):
    m, n = len(grid), len(grid[0])
    guards = {'>': (0,1), '<': (0,-1), '^': (1,0), 'v': (-1,0)}

    def fill(row, col, drow, dcol):
        row += drow
        col += dcol
        while 0 <= row < m and 0 <= col < n and grid[row][col] == '.':
            grid[row][col] = '1'
            row += drow
            col += dcol


    for row in range(m):
        for col in range(n):
            if grid[row][col] in guards:
                drow, dcol = guards[grid[row][col]]
                fill(row, col, drow, dcol)
    
    for row in range(m):
        for col in range(n):
            if grid[row][col] in guards or grid[row][col] == 'X':
                grid[row][col] = '1'
            if grid[row][col] == 'A':
                start = (row, col)
    
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = [[False]*n for _ in range(m)]
    print(grid)
    can = False
    def dfs(row, col):
        nonlocal can
        
        if row == m - 1 and col == n - 1:
            can = True
            return
        
        visited[row][col] = True
        for drow, dcol in dir:
            row += drow
            col += dcol

            if 0 <= row < m and 0 <= col < n:
                if grid[row][col] != '1' and not visited[row][col]:
                    dfs(row, col)

    dfs(*start)

    return can


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
can_reach(grid6)



# %%

def nIslands(grid):
    m, n = len(grid), len(grid[0])
    dir = [(0,1),(0,-1),(1,0),(-1,0)]

    def dfs(row, col):
        grid[row][col] = '0'

        for dy, dx in dir:
            nrow = row + dy
            ncol = col + dx

            if 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] == '1':
                dfs(nrow, ncol)
    
    n_islands = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == '1':
                n_islands += 1
                dfs(row, col)
    
    return n_islands
# %%
# %%
# Given an array of pairs of currencies like [(GBP, USD), (USD,EUR)] and a start and end currency like GBP, EUR. 
# Can you provide a python algorithm that determines whether you get from start to end currency
from collections import defaultdict
from math import log, exp

def can_convert(arr, start, end):
    # Build graph
    graph = defaultdict(list)
    for a, b, price in arr:
        graph[a] += [(b, price)]

    visited = set()
    # can = False
    def dfs(cur):
        # nonlocal can
        if cur == end:
            # can = True
            return True

        visited.add(cur)
        for b, _ in graph[cur]:
            if b not in visited:
                return dfs(b)

    can = dfs(start)
    return can if can else False

pairs = [
    ("GBP", "USD", 5),
    ("USD", "EUR", 2),
    ("GBP", "EUR", 10),
]
can_convert(pairs, 'USD', 'EUR')
# %%

# Given an array of pairs of currencies with exchange rate like [(GBP, USD, price), (USD,EUR, price)] and a start and end currency like GBP, EUR. 
# Can you provide a python algorithm that determines whether you get from start to end currency

def cheapest_conversion(arr, start, target):
    graph = defaultdict(list)
    currencies = set()
    for a, b, price in arr:
        graph[a] += [(b, log(price))]
        currencies.add(a)
        currencies.add(b)

    dist = {cur: float('inf') for cur in currencies}
    pred = {}

    if start not in currencies or target not in currencies:
        return 'Cannot reach'
    dist[start] = 0
    
    for _ in range(len(currencies) - 1):
        updated = False
        for u in graph:
            for v, weight in graph[u]:
                if dist[u] != float('inf') and dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    pred[v] = u
                    updated = True
        if not updated:
            break
    
    if dist[target] == float('inf'):
        return 'Cannot reach'
    
    path = []
    cur = target
    while cur != start:
        path.append(cur)
        cur = pred[cur]
    path.append(start)
    return path[::-1], exp(dist[target])



pairs = [
    ("GBP", "USD", 5),
    ("USD", "EUR", 1),
    ("GBP", "EUR", 10),
]
cheapest_conversion(pairs, 'GBP', 'EUR')
# %%
# Given an array of pairs of currencies with exchange rate like [(GBP, USD, price), (USD,EUR, price)] 
# Can you find arbitrage

def find_arbitrage(arr):
    graph = defaultdict(list)
    currencies = set()
    for a, b, price in arr:
        graph[a] += [(b, -log(price))]
        currencies.add(a)
        currencies.add(b)

    dist = {cur: 0 for cur in currencies}
    pred = {}

    for _ in range(len(currencies) - 1):
        updated = False
        for u in graph:
            for v, weight in graph[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    pred[v] = u
                    updated = True
        if not updated:
            break
    
    arbitrage = False
    for u in graph:
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                end = v
                arbitrage = True
    
    if not arbitrage:
        return 'No arbitrage'
    
    path = [end]
    cur = pred[end]
    while cur != end:
        path.append(cur)
        cur = pred[cur]
    
    return path[::-1]


rates = [
    ("USD", "EUR", 0.9),
    ("EUR", "GBP", 0.8),
    ("GBP", "USD", 1.5)
]

find_arbitrage(rates)
# %%
# Given array arr and target k, find number of 
# subarrays with sum == k

arr = [1,2,3,0]
k = 3

# Should return 3 for [1,2],[3],[3,0]