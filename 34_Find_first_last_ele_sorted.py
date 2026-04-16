class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        # Want first index with num[index1] > target and last index with num[index2] < target to output [idxex2 + 1, index1 - 1]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else: 
                right = mid

        start = left
        if nums[start] != target:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else: 
                left = mid
        end = left
        
        return [start, end]
                