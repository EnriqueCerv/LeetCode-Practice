def removeDuplicates(self, nums):
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
        nums=nums[k:]
        # return k
        