# %%
# Given an array of pairs of currencies like [(GBP, USD), (USD,EUR)] and a start and end currency like GBP, EUR. 
# Can you provide a python algorithm that determines whether you get from start to end currency
# %%
def can_convert(pairs, start, end):
    graph = {}
    for curr_a, curr_b in pairs:
        graph.setdefault(curr_a, []).append(curr_b)
        # # Equivalent to
        # if curr_a not in graph:
        #     graph[curr_a] = [curr_b]
        # else:
        #     graph[curr_a].append(curr_b)
    
    visited = set()
    can_reach = False

    def dfs(curr):
        nonlocal can_reach
        if curr == end:
            can_reach = True
            return
        if curr in visited:
            return
        visited.add(curr)
        for new_curr in graph.get(curr, []):
        # Equivalent to [] if curr not in graph, else graph[curr]
            dfs(new_curr)
    
    dfs(start)
    return can_reach

# %%
pairs = [("GBP", "USD"), ("USD", "EUR")]
print(can_convert(pairs, "GBP", "EUR"))
print(can_convert(pairs, "EUR", "GBP"))
print(can_convert(pairs, "USD", "SGD"))
# %%
# Given an array of pairs of currencies with exchange rate like [(GBP, USD, price), (USD,EUR, price)] and a start and end currency like GBP, EUR. 
# Can you provide a python algorithm that determines whether you get from start to end currency

import heapq

def cheapest_conversion(pairs, start, end):
    graph = {}
    for curr_a, curr_b, price in pairs:
        graph.setdefault(curr_a, []).append((curr_b, price))

    pq = [(0, start)]
    visited = {}

    while pq:
        cost, curr = heapq.heappop(pq)
        if curr == end:
            return cost
        if curr in visited and cost >= visited[curr]:
            continue
        visited[curr] = cost

        for new_curr, price in graph.get(curr, []):
            heapq.heappush(pq, (cost + price, new_curr))
    
    return 'Unreachable'
# %%
pairs = [
    ("GBP", "USD", 5),
    ("USD", "EUR", 2),
    ("GBP", "EUR", 10),
]
print(cheapest_conversion(pairs, "GBP", "EUR"))
print(cheapest_conversion(pairs, "GBP", "SGD"))
# %%
# Given an array of pairs of currencies with exchange rate like [(GBP, USD, price), (USD,EUR, price)] 
# Can you find arbitrage

from math import log

def find_arbitrage(pairs):
    # Build graph:
    graph = {}
    for curr_a, curr_b, price in pairs:
        lograte = - log((price))
        graph.setdefault(curr_a, []).append((curr_b, lograte))
    
    # Initialise currencies
    currencies = list(graph.keys())
    dist = {curr: float('inf') for curr in currencies}
    
    # Pick start currency
    start = currencies[0]
    dist[start] = 0

    for _ in range(len(currencies) - 1):
        for curr_a in graph:
            for curr_b, lograte in graph[curr_a]:
                if dist[curr_a] + lograte < dist[curr_b]:
                    dist[curr_b] = dist[curr_a] + lograte
    
    for curr_a in graph:
        for curr_b, lograte in graph[curr_a]:
            if dist[curr_a] + lograte < dist[curr_b]:
                return True
    
    return False
# %%
rates = [
    ("USD", "EUR", 0.9),
    ("EUR", "GBP", 0.8),
    ("GBP", "USD", 1.5)
]

find_arbitrage(rates)
