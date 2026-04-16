class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 0:
            return 0

        haul1 = [-1]*(n-1)
        nums1 = nums[:n-1]
        haul2 = [-1]*(n-1)
        nums2 = nums[1:]

        def backtrack(idx, arr, haul):
            if idx >= len(arr):
                return 0
            if haul[idx] != -1:
                return haul[idx]
            
            leave = backtrack(idx+1, arr, haul)
            rob = backtrack(idx+2, arr, haul) + arr[idx]
            haul[idx] = max(leave, rob)
            return haul[idx]

        backtrack(0, nums1, haul1)
        backtrack(0, nums2, haul2)

    
        return max(haul1[0], haul2[0])