# %% 209. Min size subarray sum

def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if sum(nums) < target:
            return 0

        min_length = float('inf')
        
        for i in range(n):
            cur_sum = 0
            right = i
            while right < n:
                cur_sum += nums[right]
                if cur_sum < target:
                    right += 1
                else:
                    min_length = min(min_length, right - i + 1)
                    break
        return min_length

def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # if sum(nums) < target:
        #     return 0
        
        left = 0
        right = 0
        cur_sum = 0
        min_length = float('inf')

        while left <= right and right < n:
            cur_sum += nums[right]
            print(cur_sum, left, right)
            if cur_sum >= target:
                min_length = min(min_length, right - left + 1)
                cur_sum -= nums[left]
                cur_sum -= nums[right]
                left += 1
            else:
                right += 1

            # cur_sum += nums[right]

        return min_length

nums = [12,28,83,4,25,26,25,2,25,25,25,12]
nums = [1,2,3,4,5]
target = 11
minSubArrayLen(target, nums)
