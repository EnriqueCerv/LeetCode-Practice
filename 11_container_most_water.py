# %% 11 container with most water   

def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        leftMax = 0
        right = n - 1
        rightMax = 0
        water = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            water = max(water, min(leftMax, rightMax) * (right - left))

            if leftMax < rightMax:
                left += 1
            else:
                right -= 1

        return water

def maxArea(height):
        n = len(height)
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

