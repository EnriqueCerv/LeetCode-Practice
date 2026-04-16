class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {i + 1 : float('inf') for i in range(n)}
        dist[k] = 0

        for _ in range(n - 1):
            updated = False
            for u, v, w in times:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
        
        return -1 if any(d == float('inf') for d in dist.values()) else max(dist.values())