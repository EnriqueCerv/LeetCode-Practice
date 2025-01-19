# %%

# Purely recursive knapsack problem with objects of weight in weights and value in value, and total capacity W
def knapsackRec(weights, values, W, idx):

    if idx < 0 or W <= 0:
        return 0

    if weights[idx] > W:
        return knapsackRec(weights, values, W, idx - 1)
    
    else:
        opt1 = values[idx] + knapsackRec(weights, values, W - weights[idx], idx - 1)
        opt2 = knapsackRec(weights, values, W, idx - 1)
        return max(opt1, opt2)


weights = [4,5,1]
values = [1,2,3]
W = 4
idx = len(weights) - 1

knapsackRec(weights, values, W,idx)

# %%

# Recursive knapsack but with memoization
def knapsackMemo(weights, values, W):
    n = len(weights)
    memo = [[-1 for i in range(W+1)] for i in range(n)]
    return knapsackMemoRec(weights, values, W, n - 1, memo)

def knapsackMemoRec(weights, values, W, idx, memo):
    if idx < 0 or W <= 0:
        return 0

    if memo[idx][W] != -1:
        return memo[idx][W]
    
    if weights[idx] > W:
        memo[idx][W] = knapsackMemoRec(weights, values, W, idx - 1, memo)
    
    else:
        opt1 = values[idx] + knapsackMemoRec(weights, values, W - weights[idx], idx - 1, memo)
        opt2 = knapsackMemoRec(weights, values, W, idx - 1, memo)

        memo[idx][W] = max(opt1, opt2)
    
    return memo[idx][W]

knapsackMemo(weights, values, W)


# %%
