class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        p_freq = Counter(p)
        starts = []

        for i in range(len(s) - len(p) + 1):
            sub_freq = Counter(s[i : i + len(p)])
            if sub_freq == p_freq:
                starts.append(i)
        
        return starts
        # p_len = len(p)
        # p_freq = {}
        # for char in p:
        #     if char not in p_freq:
        #         p_freq[char] = 1
        #     else:
        #         p_freq[char] += 1

        # starts = []
        # sub_freq = {}
        # left = 0
        # for right in range(len(s) - p_len + 1):
        #     if right > p_len - 1:
        #         if sub_freq[s[left]] == 1:
        #             sub_freq.pop(s[left])
        #         else:
        #             sub_freq[s[left]] -= 1
        #         left += 1
            
        #     if s[right] not in sub_freq:
        #         sub_freq[s[right]] = 1
        #     else:
        #         sub_freq[s[right]] += 1
            
        #     if sub_freq == p_freq:
        #         starts.append(left )
            
        # return starts