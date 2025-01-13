# %% 42 trapping rain water


def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        leftHeight = [0]*n
        leftMax = 0
        rightHeight = [0]*n
        rightMax = 0

        for i in range(n):
            leftMax = max(height[i], leftMax)
            leftHeight[i] += leftMax

            rightMax = max(height[-i-1], rightMax)
            rightHeight[-1-i] += rightMax
        
        trappedWater = [min(leftHeight[i], rightHeight[i]) - height[i] for i in range(n)]
        return sum(trappedWater)

        