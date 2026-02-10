# %%
# Problem Description

# You are given a list of currencies and a list of available direct currency conversions.
# Each conversion allows you to convert from one currency to another.

# Your task is to determine whether it is possible to convert from one given currency 
# to another, using zero or more intermediate conversions.
# %%
from typing import Optional
from collections import defaultdict

#%%
def canConvert(conversions, start, target):
    graph = defaultdict(list)

    for a, b in conversions:
        graph[a].append(b)
    
    def dfs(cur_curr, visited):
        if cur_curr == target:
            return True

        visited.add(cur_curr)
        for curr in graph[cur_curr]:
            if curr not in visited:
                if dfs(curr, visited):
                    return True
        
        return False
    
    return dfs(start, set())

# %%
currencies = ["USD", "EUR", "GBP", "JPY"]

conversions = [
    ["USD", "EUR"],
    ["EUR", "GBP"],
    ["GBP", "JPY"]
]

start = "USD"
target = "JPY"

canConvert(conversions, start, target)
# %%
currencies = ["USD", "EUR", "JPY"]

conversions = [
    ["USD", "EUR"],
    ["JPY", "USD"]
]

start = "EUR"
target = "JPY"

canConvert(conversions, start, target)