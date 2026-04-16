def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        max_length = 0
        left = 0
        freq = Counter()

        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(freq.values())

            if (right - left + 1) > max_freq + k:
                freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length