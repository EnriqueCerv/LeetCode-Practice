class Solution:
    def numDecodings(self, s: str) -> int:

        n_ways = {}

        def backtrack(st):
            if len(st) == 0:
                return 1  

            if st[0] == '0':
                return 0 

            if st in n_ways:
                return n_ways[st]
            
            cur_ways = backtrack(st[1:])

            if len(st) >= 2 and 10 <= int(st[:2]) <= 26:
                cur_ways += backtrack(st[2:])
            
            n_ways[st] = cur_ways
            return cur_ways
        
        return backtrack(s)