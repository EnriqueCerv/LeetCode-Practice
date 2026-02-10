# %%
def letterCombinations(self, digits: str) -> List[str]:
        # n = len(digits)
        # combos = set()
        # digit_to_letter = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ## DP approach
        # def backtrack(st, idx):
        #     if idx == n:
        #         combos.add(st)
        #         return
            
        #     cur_num = int(digits[idx])
        #     for char in digit_to_letter[cur_num - 2]:
        #         backtrack(st + char, idx + 1)
            
        # backtrack('', 0)
        # return list(combos)

        ## Backtrack approach
        n = len(digits)
        combos, cur_combo = [], []
        digit_to_letter = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        def backtrack(idx):
            if idx == n:
                combos.append(''.join(cur_combo))
                return
            
            cur_num = int(digits[idx])
            for char in digit_to_letter[cur_num - 2]:
                cur_combo.append(char)
                backtrack(idx + 1)
                cur_combo.pop()
        
        backtrack(0)
        return combos