# %%
# In a day, an account holder at HackerBank wants to make n transactions. 
# In each transaction, money is either sent (negative amount) or received (positive amount).
# Given n transactions, the transactions occur in order from 1 through n, but transactions may be skipped.
# The balance starts at 0 and is the running sum of the selected transactions. 
# It can never go negative. 
# Find out the maximum number of transactions possible. 

transactions = [3,2,-5,-6,-1,4]
# Should return 4 for for transactions 1,2,3,6.
transactions = [-5, 10, -3, 7, -8, 2]
# Should return 5 for 10,-3,7,-8,2

# %%
def max_transactios(arr):

    n = len(arr)
    trans = {}

    def rec(i, cur_amount):
        if i == n:
            return 0
        if (i, cur_amount) in trans:
            return trans[(i, cur_amount)]

        do = 1 + rec(i + 1, cur_amount + arr[i]) if cur_amount + arr[i] >=0 else 0
        skip = rec(i + 1, cur_amount)
        trans[(i, cur_amount)] = max(do, skip)
        return trans[(i, cur_amount)]

    return rec(0,0)

max_transactios(transactions)

# %%
# Better solution using heap queue

import heapq
def max_transactions(arr):
    balance = 0
    heap = []

    for x in arr:
        balance += x
        heapq.heappush(heap, x)

        if balance < 0:
            worst_neg_transaction = heapq.heappop(heap)
            balance -= worst_neg_transaction
    
    return len(heap)

max_transactions(transactions)
   
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

