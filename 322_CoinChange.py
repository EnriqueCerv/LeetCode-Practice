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

def coinCHange(self, coins, amount):
        combos = {}

        def backtrack(am):
            if am == 0:
                combos[am] = 0
                return 0
            elif am < 0:
                combos[am] = float('inf')
                return float('inf')
            
            if am in combos:
                return combos[am]
            
            possibilities = [backtrack(am - coin) for coin in coins]
            combos[am] = 1 + min(possibilities)
            return combos[am]
        
        backtrack(amount)
        return -1 if combos[amount] == float('inf') else combos[amount]