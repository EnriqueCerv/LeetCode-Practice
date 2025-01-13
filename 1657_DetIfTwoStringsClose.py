# %%
def closeStrings(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        from collections import Counter
        
        dict1 = dict(Counter(word1))
        dict2 = dict(Counter(word2))

        keys1 = set(dict1.keys())
        keys2 = set(dict2.keys())

        freq1 = list(dict1.values())
        freq1.sort()
        freq2 = list(dict2.values())
        freq2.sort()

        return True if freq1 == freq2 and keys1 == keys2 else False

word1 = 'uau'
word2 = 'ssx'

closeStrings(word1,word2)