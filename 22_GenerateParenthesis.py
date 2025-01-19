def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(open, close, string):
            if open > n or close > n or open < close:
                return

            if open == n and close == n:
                combinations.append(string)
                return
            
            backtrack(open + 1, close, string + '(')
            backtrack(open, close + 1, string + ')')
        
        combinations = []
        backtrack(0,0,'')
        return combinations