# %% 42 trapping rain water


def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_max = [0]*n
        left_cur_max = 0
        right_max = [0]*n
        right_cur_max = 0
        for i in range(n):
            left_max[i] = max(height[i], left_cur_max)
            if height[i] >= left_cur_max:
                left_cur_max = height[i]
            right_max[-1-i] = max(height[-1-i], right_cur_max)
            if height[-1-i] >= right_cur_max:
                right_cur_max = height[-1-i]
            # left_max[i] = max(max(left_max), height[i])
            # right_max[-1-i] = max(max(right_max), height[-1-i])
        water = sum([min(left_max[i],right_max[i]) - height[i] for i in range(n)])
        return water