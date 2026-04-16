class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left, right = 1, max(piles)

        def hour_per_speed(k):
            return sum(ceil(pile/k) for pile in piles)
        
        while left < right:
            mid = (left + right) // 2
            time = hour_per_speed(mid)

            if time <= h:
                right = mid
            else:
                left = mid + 1
        
        return left