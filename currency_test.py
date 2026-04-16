# %%
from collections import Counter, defaultdict
import numpy
from numpy import log, exp
# %%
# Given list of available currency exchanges, start currency and end currency, see if you can get from start to end

def can_convert(fx, start, end):
    graph = defaultdict(list)
    for u, v, _ in fx:
        graph[u].append(v)
    
    visited = set()

    def dfs(curr):
        nonlocal end
        if curr == end:
            return True

        visited.add(curr)
        for nbor in graph[curr]:
            if nbor not in visited:
                return dfs(nbor)

    return dfs(start) or False


pairs = [
    ("GBP", "USD", 5),
    ("USD", "EUR", 2),
    ("GBP", "EUR", 10),
    ("JPY", 'GBP', 5)
]
can_convert(pairs, 'GBP', 'JPY')


# %%
# Given list of available currency exchanges, start currency and end currency, find cheapest exchange

def cheapest_fx(fx, start, end):
    dist = {}
    pred = {}
    for u, v, _ in fx:
        if u not in dist:
            if u == start:
                dist[u] = 0
            else:
                dist[u] = float('inf')
        if u not in pred:
            pred[u] = None
        if v not in dist:
            if v == start:
                dist[v] = 0
            else:
                dist[v] = float('inf')
        if v not in pred:
            pred[v] = None
    
    for _ in range(len(dist) - 1):
        updated = False

        for u, v, price in fx:
            logprice = log(price)
            if dist[v] > dist[u] + logprice:
                dist[v] = dist[u] + logprice
                pred[v] = u
                updated = True
        
        if not updated:
            break
    
    path = [end]
    node = end
    while node != start:
        node = pred[node]
        path.append(node)
    
    return path[::-1], exp(dist[end])

pairs = [
    ("GBP", "USD", 5),
    ("GBP", "JPY", 2),
    ("JPY", "USD", 2),
    ("USD", "EUR", 5),
    ("USD", "EUR", 1),
    ("GBP", "EUR", 10),
]

cheapest_fx(pairs, 'JPY', 'EUR')
    

# %%

# Given list of available currency exchanges, start currency and end currency, find arbitrage

def arbitrage_fx(fx):
    dist = {}
    pred = {}
    for u, v, _ in fx:
        if u not in dist:
            dist[u] = 0
            pred[u] = None
        if v not in dist:
            dist[v] = 0
            pred[v] = None
    
    for _ in range(len(dist) - 1):
        updated = False

        for u, v, price in fx:
            logprice = log(price)
            if dist[v] > dist[u] - logprice:
                dist[v] = dist[u] - logprice
                pred[v] = u
                updated = True
        
        if not updated:
            break
    
    start = None
    for u, v, price in fx:
        logprice = log(price)
        if dist[v] > dist[u] - logprice:
            start = v

    if start is None:
        return 'No arbitrage detected'
    
    node = start
    for _ in range(len(pred)):
        node = pred[node]

    seen = set()
    path = []
    while node not in seen:
        seen.add(node)
        path.append(node)
        node = pred[node]
    
    return 'Abitrage in loop', path[::-1]

rates = [
    ("USD", "EUR", 0.9),
    ("EUR", "GBP", 0.8),
    ("GBP", "USD", 1.5)
]
rates = [
    # Main currencies
    ("USD", "EUR", 0.91),
    ("EUR", "USD", 1.08),
    ("USD", "GBP", 0.79),
    ("GBP", "USD", 1.25),
    ("USD", "JPY", 149.50),
    ("JPY", "USD", 0.0067),
    ("EUR", "GBP", 0.87),
    ("GBP", "EUR", 1.14),
    ("EUR", "JPY", 164.20),
    ("JPY", "EUR", 0.0061),

    # SGD cluster — no arbitrage here
    ("USD", "SGD", 1.34),
    ("SGD", "USD", 0.74),
    ("SGD", "EUR", 0.68),
    ("EUR", "SGD", 1.46),

    # Arbitrage cycle: JPY -> GBP -> SGD -> JPY
    # 0.0067 * 148.0 * 1.013 = 1.0059... > 1
    ("JPY", "GBP", 0.0067),
    ("GBP", "SGD", 1.696),
    ("SGD", "JPY", 88.80),
]
# ```

# The hidden cycle is `JPY → GBP → SGD → JPY`:
# ```
# 0.0067 × 1.696 × 88.80 ≈ 1.008 > 1
arbitrage_fx(rates)