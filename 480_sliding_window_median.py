class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        import bisect

        window = sorted(nums[:k])
        def median(window):
            return window[k // 2] if k % 2 == 1 else (window[k // 2] + window[(k - 1) // 2]) / 2
        medians = [median(window)]

        left = 0
        for right, num_right in enumerate(nums[k:]):
            bisect.insort(window, num_right)
            window.remove(nums[left])
            
            medians.append(median(window))
            left += 1
        
        return medians