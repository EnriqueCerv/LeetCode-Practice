# %% 80 Remove duplicates from sorted array 2
nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_ele = nums[0]
        counter = 0
        j=1
        for i in range(len(nums)-1):
            if nums[j]==cur_ele:
                counter += 1
                if counter >= 2:
                    nums.pop(j)
                    j -= 1
            else:
                cur_ele = nums[j]
                counter = 0
            j+= 1
            # print(j, counter, cur_ele)
        return len(nums), nums
removeDuplicates(nums)