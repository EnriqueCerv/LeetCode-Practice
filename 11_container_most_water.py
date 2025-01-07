# %% 11 container with most water   

def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        n = len(height)
        
        # left_max = 0
        # left_max_idx = 0
        # right_max = 0
        # right_max_idx = n-1
        # for i in range(n):
        #     if left_max < height[i]:
        #         left_max = height[i]
        #         left_max_idx = i
        #     length = right_max_idx - left_max_idx
        #     water = max(water, length * min(right_max, left_max))
        #     if right_max < height[n-1-i]:
        #         right_max = height[n-1-i]
        #         right_max_idx = n-1-i
        #     # print(left_max, right_max)
        #     length = right_max_idx - left_max_idx
        #     water = max(water, length * min(right_max, left_max))
        # return water

        left = 0
        right = n-1
        water = 0
        while left < right:
            length = right - left
            water = max(water, length * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water

height = [1,8,6,2,5,4,8,3,7]
height = [1,2,4,3]
height = [2,3,4,5,18,17,6]

maxArea(height)
