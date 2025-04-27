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
# First the recursive approach

def maxTransactionsRec(transactions, balance, idx):
    n = len(transactions)
    if idx == n or balance < 0:
        return 0
    
    if transactions[idx] >= 0:
        return 1 + maxTransactionsRec(transactions, balance + transactions[idx], idx + 1)

    else:
        opt1 = maxTransactionsRec(transactions, balance, idx + 1)
        if balance + transactions[idx] >= 0:
            opt2 = 1 + maxTransactionsRec(transactions, balance + transactions[idx], idx + 1)
            opt1 = max(opt1, opt2)
        return opt1 

maxTransactionsRec(transactions, 0, 0)


# %%
# Now the memoized dp approeach

def maxTransactionsMemo(transactions, balance, idx, memo):
    n = len(transactions)

    if idx == n or balance < 0:
        memo[(idx, balance)] = 0
        return 0

    if (idx, balance) in memo:
        return memo[(idx, balance)]

    if transactions[idx] >= 0:
        memo[(idx, balance)] = 1 + maxTransactionsMemo(transactions, balance + transactions[idx], idx + 1, memo)
    else:
        opt1 = maxTransactionsMemo(transactions, balance, idx + 1, memo)
        if balance + transactions[idx] >= 0:
            opt2 = 1 + maxTransactionsMemo(transactions, balance + transactions[idx], idx + 1, memo)
            opt1 = max(opt1, opt2)
        memo[(idx, balance)] = opt1
    
    return memo[(idx, balance)]


def maxTransactionsDP(transactions):
    n = len(transactions)
    memo = {}

    return maxTransactionsMemo(transactions, 0,0,memo)

maxTransactionsDP(transactions)
# %%
# New method with a 1d memo array


def maxTransactions(arr):
    n = len(arr)
    trans = [-1]*n

    def backtrack(idx, balance):
        if idx >= n:
            return 0
        
        if trans[idx] != -1:
            return trans[idx]
        
        if balance < 0:
            return 0

        if arr[idx] >= 0:
            trans[idx] = 1 + backtrack(idx + 1, balance + arr[idx])
            return trans[idx]
        else:
            perform = 1 + backtrack(idx + 1, balance + arr[idx])
            leave = backtrack(idx + 1, balance)
            trans[idx] = max(perform, leave)
            return trans[idx]
    backtrack(0,0)
    return trans[0]


maxTransactions(transactions)