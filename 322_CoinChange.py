def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        nCoins = len(coins)
        dp = [-1]*(1 + amount)

        def backtrack(am):
            if am == 0:
                return 0
            if am < 0:
                return float('inf')
            
            if dp[am] != -1:
                return dp[am]

            options = [backtrack(am - coin) for coin in coins]
            dp[am] = 1 + min(options)
            return dp[am]
        
        backtrack(amount)
        return -1 if dp[-1] == float('inf') else dp[-1]