class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        tot_sum = sum(nums)
        if tot_sum % 2 == 1:
            return False
        target = tot_sum // 2
        seen = {}

        def rec(i, cur_sum):
            if cur_sum == target:
                return True
            if i == n or cur_sum > target:
                return False
            if (i, cur_sum) in seen:
                return seen[(i, cur_sum)]
            
            take = rec(i + 1, cur_sum + nums[i]) 
            skip = rec(i + 1, cur_sum)
            seen[(i, cur_sum)] = take or skip
            return seen[(i, cur_sum)]

        return rec(0,0)
