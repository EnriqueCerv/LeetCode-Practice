class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # DFS Approach

        def dfs(idx, cur_sum):
            if cur_sum == target:
                combos.append(cur_combo[:])
                return
            if idx == n or cur_sum > target:
                return
            
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                cur_combo.append(candidates[i])
                dfs(i + 1, cur_sum + candidates[i])
                cur_combo.pop()

        combos = []
        cur_combo = []
        n = len(candidates)
        candidates.sort()
        dfs(0,0)
        return combos

        # # DP approach

        # combos = []
        # n = len(candidates)

        # def backtrack(idx, cur_sum, cur_combo):
        #     if cur_sum == target:
        #         cur_combo.sort()
        #         if cur_combo not in combos:
        #             combos.append(cur_combo)
        #         return
        #     if idx == n or cur_sum > target:
        #         return
            
            
        #     backtrack(idx + 1, cur_sum + candidates[idx], cur_combo + [candidates[idx]])
        #     backtrack(idx + 1, cur_sum, cur_combo)
            
        # backtrack(0,0,[])
        # return combos
