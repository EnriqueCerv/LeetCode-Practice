class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # DFS Approach
        # combos = []
        # cur_combo = []

        # def dfs(left, start):
        #     if left == 0:
        #         combos.append(cur_combo[:])
        #         return

        #     for num in range(start, n + 1):
        #         cur_combo.append(num)
        #         dfs(left - 1, num + 1)
        #         cur_combo.pop()
        
        # dfs(k, 0)
        # return combos

        # DP Approach
        combos = []

        def backtrack(num, cur_combo):
            if len(cur_combo) == k:
                combos.append(cur_combo)
                return
            if num > n:
                return
            
            for num2 in range(num + 1, n + 1):
                backtrack(num2, cur_combo + [num2])
            
        for num2 in range(1, n + 1):
            backtrack(num2, [num2])
        
        return combos