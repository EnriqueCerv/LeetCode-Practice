def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxLength = 1
        lengths = [0]*n

        for i in range(n):
            previous = [lengths[j] for j in range(i) if nums[j] < nums[i]]
            # print(previous)
            if len(previous) == 0:
                maxPrevLength = 0
            else:
                maxPrevLength = max(previous)

            lengths[i] = 1 + maxPrevLength
            maxLength = max(maxLength, lengths[i])
        # print(lengths)
        return maxLength


def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        subseqs = [1]*n
        max_len = 1

        for i in range(n):
            possible = [subseqs[j] + 1 for j in reversed(range(i)) if nums[j] < nums[i]]
            if possible:
                subseqs[i] = max(possible)

            if subseqs[i] > max_len:
                max_len = subseqs[i]
        
        return max_len      


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        max_len = 1

        for i in range(n):
            possible = [dp[j] + 1 for j in reversed(range(i)) if nums[j] < nums[i]]

            if possible:
                dp[i] = max(possible)
            
            max_len = max(max_len, dp[i])

        return max_len
