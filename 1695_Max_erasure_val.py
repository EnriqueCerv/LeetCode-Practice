def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum, cur_sum = 0, 0
        left = 0
        freq = set()

        for right in range(len(nums)):
            nright = nums[right]
            while nright in freq:
                nleft = nums[left]
                cur_sum -= nleft
                freq.remove(nleft)
                left += 1
            
            cur_sum += nright
            freq.add(nright)
            if max_sum < cur_sum:
                max_sum = cur_sum
            # max_sum = max(max_sum, cur_sum)
    
        return max_sum