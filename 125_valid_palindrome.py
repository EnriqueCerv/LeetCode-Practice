# %% 125 valid palindrome
def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        st = ''.join([i for i in s if i.isalpha()])
        st = st.lower()
        reverse_st = st[::-1]
        return st == reverse_st

s = "A man, a plan, a canal: Panama"
isPalindrome(s)


