class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        seen = {}

        def rec(cur_amount, i):
            if cur_amount == 0:
                return 1
            if (cur_amount, i) in seen:
                return seen[(cur_amount, i)]
            
            use = rec(cur_amount - coins[i], i) if cur_amount - coins[i] >= 0 else 0
            skip = rec(cur_amount, i + 1) if i + 1 < len(coins) else 0
            seen[(cur_amount, i)] = use + skip
            
            return seen[(cur_amount, i)]

        return rec(amount, 0)