class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        new_edges = []
        for u, v, w in edges:
            new_edges.append([u, v, w])
            new_edges.append([v, u, w])
        
        def BF(start):
            dist = [float('inf')] * n
            dist[start] = 0

            for _ in range(n - 1):
                updated = False
                for u, v, w, in new_edges:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        updated = True

                if not updated:
                    break
            
            n_reach = sum(1 for i in range(n) if i != start and dist[i] <= distanceThreshold)
            return n_reach
        
        min_reach = float('inf')
        for start in range(n):
            reach = BF(start)
            if reach <= min_reach:
                min_reach = reach
                ans = start

        return ans 



        