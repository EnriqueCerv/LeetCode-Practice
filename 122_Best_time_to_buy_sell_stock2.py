# %% 122 Best time to buy and sell stocks 2
prices = [7,6,4,3,1]
import itertools

def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pairs = list(itertools.pairwise(prices))
        increases = [pair[1]-pair[0] for pair in pairs]
        profit = 0
        for i in range(len(increases)):
            if increases[i]>0:
                profit += prices[i+1]-prices[i]
        return profit

def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pairs = list(itertools.pairwise(prices))
        return sum(max(0,pair[1]-pair[0]) for pair in pairs)

maxProfit(prices)