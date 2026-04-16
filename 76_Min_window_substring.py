def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        m, n = len(s), len(t)
        if n > m:
            return ''

        t_freq = Counter(t)
        min_length = float('inf')
        left = start = 0

        for right, char_right in enumerate(s):
            if char_right in t_freq:
                t_freq[char_right] -= 1

            while all(freq <= 0 for freq in t_freq.values()):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left
                char_left = s[left]
                if char_left in t_freq:
                    t_freq[char_left] += 1
                left += 1

        return '' if min_length == float('inf') else s[start : start + min_length]
