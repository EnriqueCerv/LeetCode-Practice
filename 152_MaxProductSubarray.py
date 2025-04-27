class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using Kadames algo

        curMax = nums[0]
        curMin = nums[0]
        maxProd = nums[0]

        for num in nums[1:]:
            tempMax = curMax
            tempMin = curMin

            curMax = max(num, tempMax * num, tempMin * num)
            curMin = min(num, tempMax * num, tempMin * num)

            maxProd = max(maxProd, curMax)

        return maxProd

        # Using DP
        # Too much memory
        # n = len(nums)
        # prods = [[1]*n for i in range(n)]
        # maxProd = -float('inf')
        
        # for i in reversed(range(n)):
        #     for j in range(i, n):
        #         prods[i][j] = prods[i][j-1] * nums[j]
        #         maxProd = max(maxProd, prods[i][j])

        # return maxProd