class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        # This is like the dynamic dice game
        dp = [0] * (n + 1)
        for i in range(k, n+1):
            dp[i] = 1

        running_sum = sum(dp[k : min(k + maxPts, n + 1)])
        for i in reversed(range(k)):
            dp[i] = running_sum / maxPts
            if i + maxPts <= n:
                running_sum += dp[i] - dp[i + maxPts]
            else:
                running_sum += dp[i]
        
        return dp[0]

        # states = {}

        # def backtrack(cur_points):
        #     if k <= cur_points <= n:
        #         return 1
        #     elif cur_points > n:
        #         return 0

        #     if cur_points in states:
        #         return states[cur_points]
            
        #     prob = 1/maxPts * sum(backtrack(cur_points + i) for i in range(1, maxPts + 1))
        #     states[cur_points] = prob
        #     return states[cur_points]
        
        # return backtrack(0)