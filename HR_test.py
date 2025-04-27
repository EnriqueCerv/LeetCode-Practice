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

def maxTransactions(arr):
    n = len(arr)
    dp = [-1]*(n)

    def backtrack(i, balance):
        if i == n or balance < 0:
            return 0
        if dp[i] != -1:
            return dp[i]

        if arr[i] >= 0:
            dp[i] = 1 + backtrack(i + 1, balance + arr[i])
        else:
            dp[i] = max(
                1 + backtrack(i+1, balance + arr[i]),
                backtrack(i+1, balance)
            )
        return dp[i]
    
    backtrack(0,0)
    return dp[0]

maxTransactions(transactions)