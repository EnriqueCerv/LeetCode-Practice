class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def days_per_capacity(k):
            counter = 1
            cur_weight = 0
            for weight in weights:
                if cur_weight + weight > k:
                    counter += 1
                    cur_weight = 0
                cur_weight += weight
            return counter
        
        while left < right:
            mid = (left + right) // 2
            cur_days = days_per_capacity(mid)
            
            if cur_days <= days:
                right = mid
            else:
                left = mid + 1
        
        return left