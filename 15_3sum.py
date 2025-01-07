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
            if i>0 and nums[i] == nums[i-1]:
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
