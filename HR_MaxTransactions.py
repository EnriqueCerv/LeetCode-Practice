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
# First the recursive approach

def maxTransactionsRec(transactions, balance, idx):
    n = len(transactions)
    if idx == n or balance < 0:
        return 0
    
    if transactions[idx] >= 0:
        return 1 + maxTransactionsRec(transactions, balance + transactions[idx], idx + 1)

    else:
        do = 1 + maxTransactionsRec(transactions, balance + transactions[idx], idx + 1)
        skip = maxTransactionsRec(transactions, balance, idx + 1)
        return max(do, skip)
        # opt1 = maxTransactionsRec(transactions, balance, idx + 1)
        # if balance + transactions[idx] >= 0:
        #     opt2 = 1 + maxTransactionsRec(transactions, balance + transactions[idx], idx + 1)
        #     opt1 = max(opt1, opt2)
        # return opt1 

maxTransactionsRec(transactions, 0, 0)


# %%
# Now the memoized dp approeach

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