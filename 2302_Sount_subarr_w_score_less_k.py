class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)
        cur_sum = count = 0

        left = 0
        for right in range(n):
            cur_sum += nums[right]
            
            while cur_sum * (right - left + 1) >= k:
                cur_sum -= nums[left]
                left += 1
            
            if cur_sum * (right - left + 1) < k:
                count += right - left + 1
        
        return count


        # # Tabulation without storage
        # n = len(nums)
        # count = 0

        # for i in range(n):
        #     score = nums[i]
        #     if score < k:
        #         count += 1
        #     else:
        #         continue

        #     for j in reversed(range(i)):
        #         score += nums[j]
        #         length = i - j + 1
        #         if score * length < k:
        #             count += 1
        #         else:
        #             break

        # return count
        
        # n = len(nums)
        # scores = [[0]*n for i in range(n)]
        # count = 0


        # # Full tabulation approach
        # for i in range(n):
        #     if nums[i] < k:
        #         count += 1
        #         scores[i][i] = nums[i] 
        #     else:
        #         scores[i][i] = 0

        # for i in range(n):
        #     for j in reversed(range(i)):
        #         if scores[i][j + 1] == 0:
        #             scores[i][j] = 0
        #         else:
        #             prev = scores[i][j + 1] / (i - (j + 1) + 1)
        #             new = (prev + nums[j]) * (i - j + 1)
        #             if new < k:
        #                 count += 1
        #                 scores[i][j] = new 
        #             else:
        #                 scores[i][j] = 0
        
        # return count