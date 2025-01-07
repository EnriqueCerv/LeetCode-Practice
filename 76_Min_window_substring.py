# %% 76. Min window substring

def minWindow(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)

        tDict = {}
        for ele in t:
            if ele in tDict:
                tDict[ele] += 1
            else:
                tDict[ele] = 1

        left = 0
        min_string = []

        for right in range(m):
            min_string.append(s[right])
            if s[right] in tDict:
                tDict[s[right]] -= 1
            while sum(tDict.values()) == 0 and right - left >= n:
                if s[left] in tDict:
                    tDict[s[left]] += 1
                min_string.pop(0)
                left += 1
        return ''.join(min_string)

s = "ADOBECODEBANC"
t = 'ABC'

minWindow(s,t)