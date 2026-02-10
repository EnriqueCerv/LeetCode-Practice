class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {'+', '-', '*', '/'}
        stack = []
        output = 0

        while tokens:
            item = tokens.pop(0)
            # print(stack, item)
            if item in ops:
                n2 = stack.pop()
                n1 = stack.pop()
                if item == '+':
                    stack.append(int(n1 + n2))
                elif item == '-':
                    stack.append(int(n1 - n2))
                elif item == '*':
                    stack.append(int(n1 * n2))
                else:
                    # print(n1, n2, int(n1/n2))
                    stack.append(int(n1 / n2))
                
            else:
                stack.append(int(item))
        
        return stack.pop()