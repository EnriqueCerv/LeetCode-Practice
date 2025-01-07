# %% 27 Remove element
nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        cur_ele=nums[0]
        for i in range(len(nums)):
            if nums[i]!= cur_ele:
                nums[k]=nums[i]
                k+=1
            cur_ele = nums[k-1]
        return k, nums

removeDuplicates(nums)