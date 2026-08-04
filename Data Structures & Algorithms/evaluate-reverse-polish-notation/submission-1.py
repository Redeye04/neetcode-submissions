class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:

            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            else:
                op2 = stack.pop()
                op1 = stack.pop()

                if i == '+':
                    stack.append(op1 + op2)
                    continue
                
                if i == '-':
                    stack.append(op1 - op2)
                    continue

                if i == '*':
                    stack.append(op1 * op2)
                    continue
                
                if i == '/':
                    stack.append(int(op1 / op2))
                    continue

        return stack[-1]