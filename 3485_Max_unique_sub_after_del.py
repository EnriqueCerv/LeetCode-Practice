def maxSum(self, nums: List[int]) -> int:

        taken = {}
        cur_sum = 0
        changed = False
        for i, num in enumerate(nums):
            if num >= 0 and num not in taken:
                cur_sum += num
                taken[num] = 1
                changed = True
        
        return cur_sum if changed else max(nums)