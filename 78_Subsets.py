def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        subsets_idx = []
        for i in range(2**n):
            binary = bin(i)[2:].zfill(n)
            subsets_idx.append(list(binary))

        subsets = []
        for ele in subsets_idx:
            subset = []
            for i, char in enumerate(ele):
                if char == '1':
                    subset.append(nums[i])
            subsets.append(subset)
        
        return subsets