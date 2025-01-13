def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)
        iMin = float('inf')
        jMin = float('inf')
        kMin = float('inf') 

        for i in range(n):
            if nums[i] < iMin:
                iMin = nums[i]
            elif nums[i] >= iMin + 1:
                if nums[i] < jMin:
                    jMin = nums[i]
                elif nums[i] >= jMin + 1:
                    if nums[i] < kMin:
                        kMin = nums[i]
                        
        return True if sum([iMin, jMin, kMin]) < float('inf') else False

        # for i in range(n):
        #     iCur = nums[i]
        #     if i + 1 < n:
        #         for j in range(i + 1,n):
        #             jCur = nums[j]
        #             if iCur < jCur and j + 1 < n:
        #                 for k in range(j + 1,n):
        #                     kCur = nums[k]
        #                     if jCur < kCur:
        #                         return True
        # return False