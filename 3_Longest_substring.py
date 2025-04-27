# %%
def lenfthOfLongestSubstring(s):

        # n = len(s)
        # present_chars = set()
        # left_pointer = 0
        # cur_length = 0

        # for i in range(n):
        #     char = s[i]
        #     while char in present_chars:
        #         present_chars.remove(s[left_pointer])
        #         left_pointer += 1
        #     present_chars.add(char)
        #     cur_length = max(cur_length, i - left_pointer + 1)

        # return cur_length
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0

        for right in range(n):

            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            maxLength = max(maxLength, len(charSet))
        
        return maxLength