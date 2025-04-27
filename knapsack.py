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



# %%
weights = [4,5,1]
values = [1,2,3]
W = 4
# 4

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
# 220

values = [10, 20, 30]
weights = [2, 3, 5]
W = 10
# 60

values = [100, 90, 120]
weights = [50, 40, 60]
W = 50
# 100


knapsackMemo(weights, values, W)
# %%
# %%
# Given n items where each item has some weight 
# and profit associated with it and also given a 
# bag with capacity W, 
# [i.e., the bag can hold at most W weight in it]. 
# The task is to put the items into the bag such that the 
# sum of profits 
# associated with them is the maximum possible. 
# %%
def knapsack(weight, profit, maxWeight):
    n = len(weight)
    dp = [[-1]*(maxWeight + 1) for i in range(n)]

    def backtrack(i, curWeight):
        # print(i, curWeight)
        if i == n or curWeight > maxWeight:
            return 0
            
        if dp[i][curWeight] != -1:
            return dp[i][curWeight]

        take = 0
        if curWeight + weight[i] <= maxWeight:
            take = profit[i] + backtrack(i+1, curWeight + weight[i])
        leave = backtrack(i+1, curWeight)

        dp[i][curWeight] = max(take, leave)

        return dp[i][curWeight]
    
    return backtrack(0,0)

weight = [4,5,1]
profit = [1,2,3]
maxWeight = 4
# 4

# profit = [60, 100, 120]
# weight = [10, 20, 30]
# maxWeight = 50
# # 220

profit = [10, 20, 30]
weight = [2, 3, 5]
maxWeight = 10
# 60

profit = [100, 90, 120]
weight = [50, 40, 60]
maxWeight = 50
# 100

knapsack(weight, profit, maxWeight)