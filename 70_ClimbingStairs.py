def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [-1]*(n)

        def backtrack(i):
            if i > n:
                return 0
            if i == n:
                return 1

            if steps[i] != -1:
                return steps[i]
            
            steps[i] = backtrack(i+1) + backtrack(i+2)
            return steps[i]

        backtrack(0)
        return steps[0]