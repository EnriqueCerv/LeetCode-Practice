class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [0, -prices[0] - fee] # dont own, own

        for price in prices[1:]:
            dp[0], dp[1] = max(dp[0], price + dp[1]), max(dp[1], dp[0] - price - fee)
        
        return dp[0]