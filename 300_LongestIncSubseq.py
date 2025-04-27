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