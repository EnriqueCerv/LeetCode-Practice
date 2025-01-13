def wordPattern(pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        sList = s.split(' ')
        sDict = dict()
        pDict = dict()

        for i in range(len(pattern)):
            if pattern[i] not in pDict:
                pDict[pattern[i]] = 1
            else:
                pDict[pattern[i]] += 1

            if sList[i] not in sDict:
                sDict[sList[i]] = 1
            else:
                sDict[sList[i]] += 1

            if list(sDict.values()) != list(pDict.values()):
                return False
            
        return True

pattern = 'abba'
s = 'b a a b'
wordPattern(pattern, s)