class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float('inf')]*n
        prev[src] = 0

        for _ in range(k + 1):
            curr = prev[:]
            updated = False
            for u, v, p in flights:
                if prev[u] != float('inf') and prev[u] + p < curr[v]:
                    curr[v] = prev[u] + p
                    updated = True
            prev = curr
            if not updated:
                break     
        
        return -1 if prev[dst] == float('inf') else prev[dst]