class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # DP approach
        # Too much time
        # n = len(nums)
        # sums = [[0]*n for i in range(n)]
        # counter = 0

        # for i in reversed(range(n)):
        #     for j in range(i, n):
        #         sums[i][j] = sums[i][j-1] + nums[j]
                
        #         if sums[i][j] % k == 0:
        #             counter += 1

        # return counter

        # Hashing approach
        remainderDict = {0:1}
        counter = 0
        cumuSum = 0

        for num in nums:
            cumuSum += num

            if cumuSum % k in remainderDict:
                counter += remainderDict[cumuSum % k]
                remainderDict[cumuSum % k] += 1
            else:
                remainderDict[cumuSum % k] = 1
        
        return counter
