def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        nums = [num for num in nums if num <= k]

        n = len(nums)
        counter = 0
        left = 0
        right = n - 1
        print(nums)

        while left < right:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                counter += 1
                left += 1
                right -= 1
        return counter