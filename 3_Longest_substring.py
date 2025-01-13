# %%
def lenfthOfLongestSubstring(s):

        n = len(s)
        present_chars = set()
        left_pointer = 0
        cur_length = 0

        for i in range(n):
            char = s[i]
            while char in present_chars:
                present_chars.remove(s[left_pointer])
                left_pointer += 1
            present_chars.add(char)
            cur_length = max(cur_length, i - left_pointer + 1)

        return cur_length