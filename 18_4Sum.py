def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        n = len(nums)
        nums.sort()
        quads = []

        for i in range(n-3):
            if target > 0 and nums[i] > target:
                break
            # if target < 0 and nums[i] > target:
            #     break
    
            for j in range(i+1, n - 2):
                if target > 0 and nums[i] + nums[j] > target:
                    break
                # if target < 0 and nums[i] + nums[j] > target:
                #     break

                left = j + 1
                right = n - 1
                while left < right:
                    curSum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curSum > target:
                        right -= 1
                    elif curSum < target:
                        left += 1
                    else:
                        if [nums[i], nums[j], nums[left], nums[right]] not in quads:
                            quads.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
        
        return quads