def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        f = [0]*(n+1)

        for i, char in enumerate(s, 1):
            # if char == '(':
            #     f[i] = 0
            # else:
            if char == ')':
                if i > 1 and s[i - 2] == '(':
                    f[i] = f[i - 2] + 2
                else:
                    correct_open = i - f[i-1] - 1
                    if correct_open > 0 and s[correct_open - 1] == '(':
                        f[i] = f[i - 1] + 2 + f[correct_open - 1] 

        
        return max(f)