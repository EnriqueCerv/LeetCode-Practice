class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left = 0
        z_subarrays = 0

        for right, num_right in enumerate(nums):
            if num_right != 0:
                length = (right - 1) - left + 1
                z_subarrays += (length + 1) * length // 2
                left = right + 1

        if num_right == 0:
            length = right - left + 1
            z_subarrays += (length + 1) * length // 2
        return z_subarrays