def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        # print(nums)
        minDistance = float('inf')

        for i in range(n-2):

            left = i + 1
            right = n - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1 

                distance = abs(target - sum)
                if distance < minDistance:
                    minDistance = distance
                    closest = sum
                
                if sum == target:
                    return sum

        return closest