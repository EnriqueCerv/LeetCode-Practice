class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set([num for num in nums if num > 0])
        if not nums:
            return 1
            
        min_num = min(nums)

        if min_num > 1:
            return 1

        cur_num = min_num
        while cur_num + 1 in nums:
            cur_num += 1
        
        return cur_num + 1