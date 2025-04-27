class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # DP approach 
        # Too much mem
        # n = len(nums)
        # sums = [[0]*n for i in range(n)]
        # counter = 0

        # for i in reversed(range(n)):
        #     for j in range(i, n):
        #         sums[i][j] = sums[i][j-1] + nums[j]

        #         if sums[i][j] == k:
        #             counter+= 1
        # return counter

        from collections import Counter
        #init base case where nums = [] so the sum 0 occurs 1 time
        cumSumDict = Counter({0:1})
        cumSum = 0
        counter = 0

        for num in nums:
            cumSum += num

            # If we have seen cumSum - k already, then a subarray ending at cur position would sum to k
            # This is because
            # cumSum[i] = sum_[j=0]^i nums[i] so if there exists i' < i such that
            # cumSum[i'] = cumSum[i] - k, then
            # k = cumSum[i] - cumSum[i'] = sum_(j=i'+1)^i = cumSum[i'+1 -> i]
            counter += cumSumDict[cumSum - k]

            # Update the dictionary with current sum
            cumSumDict[cumSum] += 1

        return counter


