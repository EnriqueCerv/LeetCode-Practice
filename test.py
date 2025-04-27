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
# %%

# Given array arr and target k, find number of subarrays with sum == k

arr = [1,2,3,0]
k = 3

# Should return 3 for [1,2],[3],[3,0]

def maxArray(arr, k):
    n = len(arr)
    subs = [[0]*n for i in range(n)]
    count = 0

    # for i in range(n):
    #     subs[i][i] = arr[i]

    for i in reversed(range(n)):
        for j in range(i, n):
            subs[i][j] = arr[j] + subs[i][j-1]
            if subs[i][j] == k:
                count += 1
                # print(i,j)
    
    return count

maxArray(arr, k)