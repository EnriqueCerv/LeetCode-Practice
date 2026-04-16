class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)

        # i, j is the distance between word1[:i], word2[:j]
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        
        # if j = 0, edit distance is inserting i elements
        for i in range(l1):
            dp[i + 1][0] = i + 1
        # if i = 0, edit distance is inserting j elements
        for j in range(l2):
            dp[0][j + 1] = j + 1

        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    # 1 + min(insert, delete, cchange)
                    dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])
        
        return dp[-1][-1]