# %% 238 product of array except self
nums = [1,2,3,4]
def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_prod = 1
        right_prod = 1
        ans = [1]*n
        for i in range(n):
            ans[i] = left_prod
            left_prod *= nums[i]
        for i in reversed(range(n)):
            ans[i] *= right_prod
            right_prod *= nums[i]
        return ans
productExceptSelf(nums)