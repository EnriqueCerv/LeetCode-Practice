# %% 392 is subsequence
def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = [char for char in s]
        t = [char for char in t]

        while len(s) > 0:

            if len(t) == 0 or len(t) < len(s):
                return False

            if t[0] == s[0]:
                s.pop(0)
            t.pop(0)
        
        return True

s = "b"
t = "abc"
isSubsequence(s,t)

