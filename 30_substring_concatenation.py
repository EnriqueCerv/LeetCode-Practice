class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words[0])

        ans = []
        st = 0
        
        while st < n - m * len(words) + 1:
            missing = words[:]
            cur_st = st

            while s[cur_st: cur_st + m] in missing:
                missing.remove(s[cur_st: cur_st + m])
                cur_st += m
            
            if len(missing) == 0:
                ans.append(st)
            
            st += 1
        
        return ans

