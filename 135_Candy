
# %%
def candy(ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        n = len(ratings)
        left = [1]*n
        right = [1]*n

        for i in range(n-1):
            if ratings[i+1] > ratings[i]:
                left[i+1] = 1 + left[i]
        for i in reversed(range(n-1)):
            if ratings[i] > ratings[i+1]:
                right[i] = 1 + right[i+1]
        # sum = 0
        # for i in range(n):
        #     sum += max(left[i],right[i])
        candy = [max(left[i],right[i]) for i in range(n)]
        return sum(candy)
        # return sum
# %%
