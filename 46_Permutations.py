class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # DFS Approach
        permutations = []
        n = len(nums)
        cur_permutation = []

        def dfs(leftover):
            if not leftover:
                permutations.append(cur_permutation[:])
                return
            
            for idx, num in enumerate(leftover):
                cur_permutation.append(num)
                leftover.pop(idx)
                dfs(leftover)
                cur_permutation.pop()
                leftover.insert(idx, num)
        dfs(nums)
        return permutations


        # # DP Approach
        # permutations = []

        # def backtrack(cur_permutation, leftover):
        #     if len(leftover) == 0:
        #         # if cur_permutation not in permutations:
        #         permutations.append(cur_permutation)
        #         return
            
        #     for idx, num in enumerate(leftover):
        #         temp_perm = leftover[:]
        #         temp_perm.pop(idx)
        #         backtrack(cur_permutation + [num], temp_perm)
        
        # backtrack([], nums)
        # return permutations
