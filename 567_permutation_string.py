def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_len, s2_len = len(s1), len(s2)
        s1_freq = Counter(s1)

        s2_freq = {}
        for char in s2[:s1_len]:
            if char in s1_freq:
                if char not in s2_freq:
                    s2_freq[char] = 1
                else:
                    s2_freq[char] += 1
        
        if s1_freq == s2_freq:
            return True

        left = 0
        right = s1_len
        while right < s2_len:
            char_left, char_right = s2[left], s2[right]
            if char_left in s1_freq:
                if s2_freq[char_left] == 1:
                    s2_freq.pop(char_left)
                else:
                    s2_freq[char_left] -= 1
            if char_right in s1_freq:
                if char_right not in s2_freq:
                    s2_freq[char_right] = 1
                else:
                    s2_freq[char_right] += 1
            if s1_freq == s2_freq:
                return True
            
            left += 1
            right += 1
    
        return False