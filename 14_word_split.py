class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(len(word) for word in strs)

        for i in range(min_length):
            cur_char = strs[0][i]
            for word in strs:
                if word[i] != cur_char:
                    return strs[0][ : i]
        
        return strs[0][ : min_length]
