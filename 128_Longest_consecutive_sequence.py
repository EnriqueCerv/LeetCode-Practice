# %% 128 Longest consecutive sequence
def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)

        for num in num_set:
            cur_len = 1
            if num - 1 in num_set:
                continue
            while num + 1 in num_set:
                cur_len += 1
                num += 1
            max_len = max(max_len, cur_len)
        return max_len