# %% 392 is subsequence
def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        # sub = [char for char in s]
        # t = [char for char in t]
        # idx = 0
        # for i in range(len(t)):
        #     if t[idx] != sub[0]:
        #         t.pop(idx)
        #     else:
        #         idx += 1
        #         sub.pop(0)
        #     print(sub,t)
        # return ''.join(t) == s
        sub = [char for char in s]
        t = [char for char in t]
        idx = 0
        for i in range(len(t)):
            if len(sub) == 0:
                return True
            elif len(t) <= idx:
                return False
            if t[idx] != sub[0]:
                t.pop(idx)
            else:
                idx += 1
                sub.pop(0)
            # print(sub, t)
            
        return ''.join(t) == s

s = "b"
t = "abc"
isSubsequence(s,t)
