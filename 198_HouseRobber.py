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

def rob(self, nums):
        n = len(nums)
        
        if n <= 2:
            return max(nums)

        catch = [0] * n
        catch[-1] = nums[-1]
        catch[-2] = max(nums[-2], catch[-1])

        for i in reversed(range(n - 2)):
            catch[i] = max(nums[i] + catch[i + 2], catch[i + 1])
        
        return catch[0]


# def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # catch = [-1]*n
        # def backtrack(i):
        #     if i >= n:
        #         return 0
        #     if catch[i] != -1:
        #         return catch[i]

        #     take = nums[i] + backtrack(i + 2)
        #     leave = backtrack(i + 1)
        #     catch[i] = max(take, leave)
        #     return catch[i]
        
        # return backtrack(0)

        # if n <= 2:
        #     return max(nums)

        # catch = [0] * n
        # catch[-1] = nums[-1]
        # catch[-2] = max(nums[-2], catch[-1])

        # for i in reversed(range(n - 2)):
        #     catch[i] = max(nums[i] + catch[i + 2], catch[i + 1])
        
        # return catch[0]
