# %% 55 Jump game if exact jumps

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    cur_index = 1
    while cur_index + nums[cur_index] < len(nums):
        if nums[cur_index] == 0:
            break
        cur_index += nums[cur_index]
        # if cur_index<len(nums):
        #     print(cur_index, nums[cur_index])
    return cur_index == (len(nums)-1)
    # return cur_index

nums = [2,3,1,1,4]
canJump(nums)

# %% 55 Jump game

def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums[0]>=len(nums)-1 or len(nums) == 1:
            return True

        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums)-1:
                return True
        return True

def canJump(nums):
        maxReach = 0

        for idx, reach in enumerate(nums):
            if maxReach < idx:
                return False

            maxReach = max(maxReach, idx + reach)

        return maxReach >= len(nums) - 1


def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [-1]*n

        def backtrack(i):
            if i >= n-1:
                return float('inf')
            if dp[i] != -1:
                return dp[i]
            if nums[i] == 0:
                dp[i] = -float('inf')
                return dp[i]
            
            dp[i] = i + max([backtrack(i + j) for j in range(1, nums[i] + 1)])
            return dp[i]
        
        backtrack(0)
        
        if any(ele >= n-1 for ele in dp):
            return True
        else:
            return True if len(nums) == 1 else False
