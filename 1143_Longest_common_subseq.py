def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n + 1) for i in range(m + 1)]
        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    if dp[i-1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]
                    # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                if max_len < dp[i][j]:
                    max_len = dp[i][j]
                # max_len = max(max_len, dp[i][j])
        return max_len