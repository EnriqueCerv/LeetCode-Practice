def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Using Kadame's algorithm
        curSum = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            curSum = max(curSum + num, num)
            maxSum = max(maxSum, curSum)
        
        return maxSum

        # USing DP
        # n = len(nums)
        
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return nums[0]

        # sums = [[0]*n for i in range(n)]
        # maxSum = -float('inf')

        # for i in reversed(range(n)):
        #     for j in range(i, n):
        #         sums[i][j] = sums[i][j-1] + nums[j]
        #         maxSum = max(maxSum, sums[i][j])
        
        # return maxSum