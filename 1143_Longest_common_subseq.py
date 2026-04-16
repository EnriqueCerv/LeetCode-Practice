class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        max_len = 0

        for i in range(m):
            for j in range(n):

                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                    max_len = max(max_len, dp[i + 1][j + 1])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
                
        return max_len