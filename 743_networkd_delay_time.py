class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')]*n
        dist[k - 1] = 0

        for _ in range(n - 1):
            updated = False
            for u, v, t in times:
                if dist[u - 1] + t < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + t
                    updated = True
            
            if not updated:
                break
        
        min_time = -float('inf')
        for time in dist:
            min_time = max(min_time, time)
        
        return -1 if min_time == float('inf') else min_time