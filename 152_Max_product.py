class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = cur_max = cur_min = nums[0]

        for num in nums[1:]:
            prev_max = cur_max
            prev_min = cur_min

            cur_max = max(prev_max * num, prev_min * num, num)
            cur_min = min(prev_min * num, prev_max * num, num)

            max_prod = max(max_prod, cur_max)
        
        return max_prod
        # # Using dp
        # n = len(nums)
        # dp = [[1]*n for _ in range(n)]

        # max_prod = -float('inf')
        # for i in range(n):
        #     dp[i][i] = nums[i]
        #     max_prod = max(max_prod, dp[i][i])

        # for i in range(n):
        #     for j in reversed(range(i)):
        #         dp[i][j] = nums[j] * dp[i][j + 1]
        #         max_prod = max(max_prod, dp[i][j])
                
        # return max_prod