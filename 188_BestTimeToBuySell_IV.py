# %%
def maxProfit( k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """# Init DP array with k+1 possible states (no transaction up to k-transactions)
        # each with two states (holding or not holding)
        profits = [[0]*2 for i in range(k+1)]

        # Initialise the holding state to where we have bought the first stock only (ie profit = -prices[0])
        for ele in profits[1:]:
            ele[1] = -prices[0]

        # Loop through prices, starting from the second price
        for price in prices[1:]:
            # Iterate through the possible number of transactions:
            for j in range(k, 0, -1):
                # If not holding a stock at EOD:
                profits[j][0] = max(profits[j][0], profits[j][1] + price)
                #i.e. the maximum between what we werent holding in the first place, or we were holding with profit profits[j][1] and 
                # sold to get price[i] monyes

                # If holding a stock at EOD:
                profits[j][1] = max(profits[j][1], profits[j-1][0] - price)
                #i.e. the maximum between what we weren holding in the first place, or we were not holding with one less transactionn profits[j-1][1]
                # and bought with price[i] monyes to add an extra transaction

        # Max profit after the k transactions is simply
        return profits[k][0]