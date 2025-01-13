def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        def nVowels(subS):
            nVowels = 0
            for char in subS:
                if char in vowels:
                    nVowels += 1
            return nVowels

        left = 0
        right = k
        curVowels = nVowels(s[left:right])
        maxVowels = curVowels

        while right < n:
            if s[left] in vowels:
                curVowels -= 1
            if s[right] in vowels:
                curVowels += 1
            maxVowels = max(maxVowels, curVowels)
            left += 1
            right += 1
        
        return maxVowels