def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nDelete = 0
        left = right = 0

        while right < n:
            if nums[right] == 0:
                nDelete += 1
            right += 1
            
            if nDelete > 1:
                if nums[left] == 0:
                    nDelete -= 1
                left += 1
        return right - left - 1