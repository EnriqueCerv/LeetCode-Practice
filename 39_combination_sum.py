class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # # DF Approach
        # def dfs(idx, cur_sum):
        #     if cur_sum == 0:
        #         combos.append(cur_comb[:])
        #         return
        #     if idx == n or cur_sum < 0:
        #         return
            
        #     # leave
        #     dfs(idx + 1, cur_sum)
        #     # include but stay
        #     cur_comb.append(candidates[idx])
        #     dfs(idx, cur_sum - candidates[idx])
        #     cur_comb.pop()
        
        # n = len(candidates)
        # combos = []
        # cur_comb = []
        # dfs(0,target)
        # return combos

        # DP Approach
        combos = []
        n = len(candidates)
            
        def backtrack(idx, cur_sum, cur_combo):
            if cur_sum == target and cur_combo not in combos:
                combos.append(cur_combo)
                return
            if idx == n or cur_sum > target:
                return
            
            backtrack(idx + 1, cur_sum, cur_combo)
            backtrack(idx, cur_sum + candidates[idx], cur_combo + [candidates[idx]])
            # backtrack(idx + 1, cur_sum + candidates[idx], cur_combo + [candidates[idx]])
        backtrack(0,0,[])
        return combos