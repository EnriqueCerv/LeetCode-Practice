def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        isPalindrome = [[1 for j in range(n)] for i in range(n)]
        startIdx = 0
        maxLength = 1

        for i in range(n-2, -1, -1):
            for j in range(i+1,n):
                isPalindrome[i][j] = 0
                # curString = s[i:j+1]
                # if curString == curString[::-1]:
                if s[i] == s[j] and isPalindrome[i+1][j-1]:
                    isPalindrome[i][j] = 1
                    if maxLength < j - i + 1:
                        maxLength = j - i + 1
                        startIdx = i
        
        
        return s[startIdx : startIdx + maxLength]
