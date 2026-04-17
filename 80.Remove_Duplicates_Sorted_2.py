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


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        valid_idx = 1
        prev_num = nums[0]
        counter = 1

        for num in nums[1:]:
            if num!= prev_num:
                nums[valid_idx] = num
                prev_num = num
                counter = 1
                valid_idx += 1
            else:
                if counter == 1:
                    nums[valid_idx] = num
                    valid_idx += 1
                    counter += 1
                    
        return valid_idx
