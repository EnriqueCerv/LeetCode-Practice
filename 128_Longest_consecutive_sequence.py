# %% 128 Longest consecutive sequence
def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = {num for num in nums}
        counter = 0
        for num in nums:
            cur_counter = 1
            while num + 1 in nums:
                cur_counter += 1
                num += 1
            counter = max(counter, cur_counter)
        return counter