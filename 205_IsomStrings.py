
# %%
def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = dict()
        tDict = dict()

        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = 1
            else:
                sDict[s[i]] += 1

            if t[i] not in tDict:
                tDict[t[i]] = 1
            else:
                tDict[t[i]] += 1
                
            if list(sDict.values()) != list(tDict.values()):
                return False
        return True

s = 'paper'
t = 'title'
isIsomorphic(s,t)


