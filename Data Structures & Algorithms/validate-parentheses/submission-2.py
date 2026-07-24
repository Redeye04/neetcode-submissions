class Solution:
    def isValid(self, s: str) -> bool:
        stacky = []
        hashy = {
            '{':'}',
            '[':']',
            '(':')'
        }
        for i in s:
            if i in ['}', ')', ']']:
                
                if not stacky:
                    return False
                
                if hashy[stacky.pop()] != i:
                    return False
                
            else:
                stacky.append(i)

        if stacky == []:
            return True

        return False