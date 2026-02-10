# %%
# Problem Description

# You are given a list of currencies and a list of exchange rates between them. 
# Each exchange rate represents the rate at which one currency can be converted 
# into another.

# An arbitrage opportunity exists if you can start with 1 unit of some currency, 
# perform a sequence of exchanges, and end up with more than 1 unit of the same 
# currency, without adding any external capital.

# Your task is to determine whether any arbitrage opportunity exists.
# %%
from collections import defaultdict
from math import log, exp
# %%
def hasArbitrage(rates):
    currencies = set()
    logrates = []
    for a, b, w in rates:
        currencies.add(a)
        currencies.add(b)
        logrates.append((a, b, -log(w)))
    
    dist = {curr: 0 for curr in currencies}

    for _ in range(len(currencies) - 1):
        updated = False
        for a, b, w in logrates:
            if dist[a] + w < dist[b]:
                dist[b] = dist[a] + w
                updated = True
        if not updated:
            break
    
    for a, b, w in logrates:
        if dist[a] + w < dist[b]:
            return True
    
    return False
    
    
    
# %%
currencies = ["USD", "EUR", "GBP"]

rates = [
    ["USD", "EUR", 0.9],
    ["EUR", "GBP", 0.8],
    ["GBP", "USD", 1.5]
]

hasArbitrage(rates)
# %% Modified so that it outputs the cycle

def hasArbitrage(rates):
    currencies = set()
    logrates = []
    for a, b, w in rates:
        currencies.add(a)
        currencies.add(b)
        logrates.append((a, b, -log(w)))
    
    dist = {curr: 0 for curr in currencies}
    pred = {curr: None for curr in currencies}

    for _ in range(len(currencies) - 1):
        updated = False
        for a, b, w in logrates:
            if dist[a] + w < dist[b]:
                dist[b] = dist[a] + w
                pred[b] = a
                updated = True
        if not updated:
            break
    
    cycle_node = None
    for a, b, w in logrates:
        if dist[a] + w < dist[b]:
            cycle_node = a
            break
    
    if cycle_node is None:
        return 'No arbitrage'

    path = []
    cur = cycle_node
    while True:
        path.append(cur)
        cur = pred[cur]
        if cur == cycle_node and len(path) > 1:
            return path
# %%
currencies = ["USD", "EUR", "GBP"]

rates = [
    ["USD", "EUR", 0.9],
    ["EUR", "GBP", 0.8],
    ["GBP", "USD", 1.5]
]

hasArbitrage(rates)