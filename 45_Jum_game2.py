# %% 45 Jump game 2

nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
# nums = nums[7:]

def jump(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0

        nums.reverse()
        max_index = 0
        for i in range(len(nums)):
            if nums[i]>= i:
                max_index = max(max_index, i)
        # return max_index, nums[max_index], nums[max_index:]

        nums = nums[max_index:]
        # print(nums)
        nums.reverse()
        return 1 + jump(nums)

jump(nums)


def jumps(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nJumps = 0
    maxReaßch = 0
    lastReach = 0

    for idx, num in enumerate(nums[:-1]):
        maxReach = max(maxReach, idx + num)

        if lastReach == idx:
            nJumps += 1
            lastReach = maxReach

    return nJumps