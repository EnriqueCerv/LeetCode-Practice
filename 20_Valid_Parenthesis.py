# %% 20: Valid Parenthesis:

def isBalanced(s):
    # Write your code here
    stack = []
    for ele in s:
        if ele == '(' or ele == '[' or ele == '{':
            stack.append(ele)
        else:
            if len(stack) == 0:
                return 'NO'
            a = ele == ')' and stack[-1] == '('
            b = ele == ']' and stack[-1] == '['
            c = ele == '}' and stack[-1] == '{'
            if a or b or c:
                stack.pop(-1)
            else:
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    return 'NO'

s = '[{()}]'
isBalanced(s)
