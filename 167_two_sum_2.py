# %% 167 two sum 2: input is sorted
def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(numbers)):
        #     if target - numbers[i] in numbers:
        #         idx = numbers.index(target - numbers[i], i+1)
        #         return i+1, idx + 1
        n = len(numbers)
        left = 0
        right = n-1
        for i in range(n):
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left+1, right+1
        

numbers = [-1,0]
target = -1
# numbers = [2,3,4]
# target = 6
twoSum(numbers, target)

