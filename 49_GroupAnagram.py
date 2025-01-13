def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        myDict = {}
        for ele in strs:
            mySet = [char for char in ele]
            mySet.sort()
            myString = ''.join(mySet)
            if myString not in myDict:
                myDict[myString] = [ele]
            else:
                myDict[myString] += [ele]
        
        return [val for val in myDict.values()]