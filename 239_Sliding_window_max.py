class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max_array = []
        # for i in range(len(nums)-k+1):
        #     max_array.append(max(nums[i : i + k]))
        
        # return max_array

        # cur_window = nums[:k]
        # cur_max = max(cur_window)
        # max_arr = [cur_max]
        # left = 0
        # right = k
        
        # while right < len(nums):
        #     left_num, right_num = cur_window.pop(0), nums[right]
        #     cur_window.append(right_num)

        #     if cur_max == left_num:
        #         cur_max = max(cur_window)
        #     cur_max = max(cur_max, right_num)

        #     max_arr.append(cur_max)

        #     left += 1
        #     right += 1

        # return max_arr

        idx_queue = deque()
        max_array = []

        for cur_idx, cur_num in enumerate(nums):
            # Remove first element of queue if it is outside the window:
            if idx_queue and cur_idx - idx_queue[0] > k - 1:
                idx_queue.popleft()

            # Remove elements in right of queue smaller than current element:
            while idx_queue and nums[idx_queue[-1]] <= cur_num:
                idx_queue.pop()

            # Add current idx:
            idx_queue.append(cur_idx)

            if cur_idx >= k-1:
                max_array.append(nums[idx_queue[0]])

    
        return max_array