class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = {0:-1}
        prefix_sum = 0
        max_len = 0

        for idx, num in enumerate(nums):
            prefix_sum += 1 if num else -1
            
            if prefix_sum in sums:
                max_len = max(max_len, idx - sums[prefix_sum])
            else:
                sums[prefix_sum] = idx
        
        return max_len