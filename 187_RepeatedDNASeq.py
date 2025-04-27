def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 10:
            return []

        occurs = {}
        ans = set()
        right = 10
        while right <= n:
            cur = s[right - 10: right]

            if cur not in occurs:
                occurs[cur] = 1
            else:
                # occurs[cur] += 1
                ans.add(cur)
            right += 1
        return list(ans)
        # return [key for key in list(occurs.keys()) if occurs[key] > 1]
