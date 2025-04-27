def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        breakable = [True] + [False]*n
        wordDict = set(wordDict)

        for i in range(n):
            breakable[i+1] = any(breakable[j] and s[j:i+1] in wordDict for j in range(i+1))
            print(breakable)

        return breakable[n]