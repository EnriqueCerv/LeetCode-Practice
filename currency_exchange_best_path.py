# %%
# Problem Description

# You are given a list of currencies and a list of direct currency conversion rates. 
# Each conversion allows you to exchange one currency into another at a given rate.

# Your task is to compute the maximum possible conversion rate from a given start 
# currency to a target currency, using any number of intermediate conversions.

# If no conversion path exists, return -1.0.
# %%
from collections import defaultdict
import heapq
from math import log, exp
# %% USING BELLMAN FORD
def bestRate(rates, start, target):

    nodes = set()
    edges = []

    for a, b, rate in rates:
        lograte = -log(rate)
        edges.append((a, b, lograte))
        nodes.add(a)
        nodes.add(b)

    dist = {node: float('inf') for node in nodes}
    dist[start] = 0

    # Relax edges |V|-1 times
    for _ in range(len(nodes) - 1):
        updated = False
        for a, b, lograte in edges:
            if dist[a] + lograte < dist[b]:
                dist[b] = dist[a] + lograte
                updated = True
        if not updated:
            break

    return -1 if dist[target] == float('inf') else exp(-dist[target])
# %%
rates = [
    ["USD", "EUR", 0.9],
    ["USD", "GBP", 0.7],
    ["GBP", "EUR", 1.4]
]

start = "USD"
target = "EUR"

bestRate(rates, start, target)
# %%
