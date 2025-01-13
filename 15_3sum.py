# %% 15. 3sum

def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()

        triples = []

        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    if [nums[i], nums[left], nums[right]] not in triples:
                        triples.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                else: 
                    left += 1
        
        return triples

nums = [0,0,0]
threeSum(nums)

        
# %%
def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        triples = []
        i = 0

        # if n == 3 and sum(nums) != 0:
        #     return []
        # elif n == 3 and sum(nums) == 0:
        #     return [nums]

        while i < len(nums) and nums[i] <= 0:
            left = i + 1
            right = n - 1

            while left < right:
                target = nums[left] + nums[right]
                if target > - nums[i]:
                    right -= 1
                elif target < - nums[i]:
                    left += 1
                else:
                    if [nums[i], nums[left], nums[right]] not in triples:
                        triples += [[nums[i], nums[left], nums[right]]]
                    left += 1
                    right = n - 1
                
            i += 1
        return triples

nums = [-2,0,1,1,2]
threeSum(nums)