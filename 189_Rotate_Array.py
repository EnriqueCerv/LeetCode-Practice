# %% 189 Rotate array
nums = [-1,-100,3,99]
k=2
def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nums1 = nums[:l-k]
        nums2 = nums[l-k:]
        nums3 = nums2 + nums1
        return nums3

rotate(nums,k)