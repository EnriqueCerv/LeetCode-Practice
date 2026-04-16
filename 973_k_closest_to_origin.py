class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return x**2 + y**2
        
        dists = {(x,y) : dist(x, y) for x, y in points}
        dists = {key : val for key, val in sorted(dists.items(), key = lambda item: item[1])}
        return list(dists.keys())[:k]