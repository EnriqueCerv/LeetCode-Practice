class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify_max(nums)

        for i in range(k):
            x = heapq.heappop_max(nums)
        
        return x