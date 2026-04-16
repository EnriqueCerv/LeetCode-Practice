# %%
# Given array of n integers, can do
# 1 Choose index i \in [n] and swap arr[i] with arr[i+1]
# 2. Each element can be swapped at most once.
# Find max sum_{i = 0} ^{n - 1} arr[i] * (i + 1) after optimal swaps

arr = [2,1,3,4]
arr = [4, 3, 2, 1]
arr = [5, 1, 4, 2]
arr = [1,5,4,2]

def swaps(arr):
    n = len(arr)
    base_sum = sum(arr[i] * (i + 1) for i in range(n))
    deltas = [max(0, arr[i] - arr[i + 1]) for i in range(n - 1)]

    prev2 = prev1 = 0

    for delta in deltas:
        cur = max(prev1, prev2 + delta)
        prev2 = prev1
        prev1 = cur
    return base_sum + prev1


swaps(arr)
# %%
# Given N, find number of positive integers for eqn 1/x + 1/y = 1/N!. 
# Return modelue 1e6 + 7

# Can do math to turn eqn into ab := (x - N!)(y - N!) = N! ^2 
# so need to count positive factor os N!^2 = p1^2a1 ... pm^2am

def count_factors(N):
    # Get prime factors of N
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            for j in range(2*i, N + 1, i):
                sieve[j] = False
    
    primes = [i for i in range(2, N + 1) if sieve[i]]
    # return primes

    result = 1
    for p in primes:
        exp = 0
        power = p
        while power <= N: 
            exp += N // power
            power *= p

count_factors(50)


# %%
# Given upgradeCost array representing in app upgrades with ith app costing upgradeCost[i] and updating functionality by 2**i. 
# Given integer budget
# Implement function that selects combination of upgrades maximizing enhancement without exceeding cost


def maximize(budget, upgradeCost):
    n = len(upgradeCost)
    seen = {}
    mod = 1e9 + 7

    def rec(idx, cur_budget):
        if idx == n:
            return 0
        if (idx, cur_budget) in seen:
            return seen[(idx, cur_budget)]

        do = 2**idx % mod + rec(idx + 1, cur_budget - upgradeCost[idx]) % mod if cur_budget - upgradeCost[idx] >= 0 else 0
        skip = rec(idx + 1, cur_budget) % mod
        seen[(idx, cur_budget)] = max(do, skip)
        return seen[(idx, cur_budget)]
    
    return rec(0, budget)

# Greedy works! Doing upgrade at idx = i is better than all upgrades up to and excluding i! (ie 2**i > sum(2**j for j in range(i)))
def maximize(budget, upgradeCost):
    upgrade = 0
    for i in reversed(range(len(upgradeCost))):
        if budget - upgradeCost[i] >= 0:
            budget -= upgradeCost[i]
            upgrade += 2**i
    
    return upgrade

upgradeCost = [10, 20, 14, 40, 50]
budget = 70
maximize(budget, upgradeCost)