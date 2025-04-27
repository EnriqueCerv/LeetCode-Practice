class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        counter = 0
        remainderDict = {0:-1}
        cumuSum = 0

        for idx, num in enumerate(nums):
            cumuSum += num

            remainder = cumuSum % k

            if remainder in remainderDict:
                if idx - remainderDict[remainder] > 1:
                    return True
            else:
                remainderDict[remainder] = idx

        return False