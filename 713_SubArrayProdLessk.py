def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        
        n = len(nums)
        curProd = 1
        counter = 0
        left = 0

        for right in range(n):
            curProd *= nums[right]

            while left <= right and curProd >= k:
                curProd = curProd / nums[left]
                left += 1
            counter += right - left + 1

        return counter