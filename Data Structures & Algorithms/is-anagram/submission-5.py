class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashy = {}
        hashy2 = {}

        for i in s:
            if i not in hashy:
                hashy[i] = 1
            else:
                hashy[i] += 1

        for j in t:
            if j not in hashy2:
                hashy2[j] = 1
            else:
                hashy2[j] += 1
        
        for j in t:
            if j in hashy and j in hashy2 and hashy[j] == hashy2[j]:
                continue
            else:
                return False
        
        return True
        