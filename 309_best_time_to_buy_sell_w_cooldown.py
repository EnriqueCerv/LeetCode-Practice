class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profits = {}

        def backtrack(idx, hold):
            if idx >= n:
                return 0
            if (idx, hold) in profits:
                return profits[(idx, hold)]
            
            if hold:
                sell = backtrack(idx + 2, 0) + prices[idx]
                keep_holding = backtrack(idx + 1, 1)
                profits[(idx, hold)] = max(sell, keep_holding)
            else:
                buy = backtrack(idx + 1, 1) - prices[idx]
                skip = backtrack(idx + 1, 0)
                profits[(idx, hold)] = max(buy, skip)
            
            return profits[(idx, hold)]
        
        return backtrack(0,0)


        # # Leetcode sol which i do not understand
        # freeze, sell, buy = 0, 0, -prices[0]

        # for price in prices[1:]:
        #     freeze, sell, buy =  (
        #         sell,
        #         max(sell, buy + price),
        #         max(buy, freeze - price)
        #     )
        
        # return sell