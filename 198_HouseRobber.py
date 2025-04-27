def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        haul = [-1]*n

        def backtrack(i):
            if i >= n:
                return 0
            if haul[i] != -1:
                return haul[i]
            rob = nums[i] + backtrack(i+2)
            leave = backtrack(i+1)
            haul[i] = max(rob, leave)
            return haul[i]
        
        backtrack(0)
        return haul[0]