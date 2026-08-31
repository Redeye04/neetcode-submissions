class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashy = {
            '{':'}',
            '[':']',
            '(':')'
        }
        
        for i in s:
            if i in ['}', ']', ')']:
                if stack and hashy[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack == []:
            return True

        return False