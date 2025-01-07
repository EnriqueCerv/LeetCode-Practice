# %% 121 Best time to buy and sell stocks
prices = [7,1,5,3,6,4]
def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            max_profit = max(max_profit, price-min_price)
            min_price = min(price, min_price)
        return max_profit, min_price
maxProfit(prices)