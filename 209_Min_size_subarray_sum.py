# %% 209. Min size subarray sum

def minSubArrayLen(target, nums):
        n = len(nums)
        
        left = 0
        cur_sum = 0
        min_length = float('inf')

        for right in range(n):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_length = min(min_length, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        if min_length == float('inf'):
            return 0
        return min_length

nums = [12,28,83,4,25,26,25,2,25,25,25,12]
nums = [1,2,3,4,5]
target = 11
minSubArrayLen(target, nums)

# %%
def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        curSum = 0
        minLength = float('inf')
        left = 0
        right = 0

        for right in range(n):
            curSum += nums[right]

            while curSum >= target:
                length = right - left + 1
                minLength = min(minLength, length)
                curSum -= nums[left]
                left += 1

        
        return 0 if minLength == float('inf') else minLength

nums = [2,3,1,2,4,3]
target = 7
minSubArrayLen(target, nums)