def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        idxDict = dict()

        for i in range(len(nums)):
            if nums[i] not in idxDict:
                idxDict[nums[i]] = i
            else:
                diff = i - idxDict[nums[i]]
                if diff <= k:
                    return True
                else:
                    idxDict[nums[i]] = i

        return False